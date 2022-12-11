import os
from django.urls import reverse_lazy
from typing import List
from django.views.generic.edit import (
    UpdateView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.contrib.auth.decorators import login_required

from users.models import (
    Associated,
)
from utils.models import (
    Order,
)

from .models import (
    Product,
    Unit,
    ProductTransaction,
    Stock,
    Profit,
    ProductCategory,
)
from .forms import (
    UnitCreateForm,
    ProductCreateForm,
    CategoryCreateForm,
    TransactionCreateForm,
    TransactionProviderCreateForm,
    OrderCreateForm,
)
from django.utils.translation import gettext_lazy as _


class DifferentMagnitudeUnitsError(BaseException):
    """
    Raised when the input and output units
    doesn't measure the same magnitude
    """
    pass


class NotEnoughStockError(BaseException):
    """
    Raised when the input and output units
    doesn't measure the same magnitude
    """
    pass


def convertUnit(input_unit, output_unit, value):
    iu = Unit.objects.get(name=input_unit)
    ou = Unit.objects.get(name=output_unit)
    if (iu.magnitude != ou.magnitude):
        raise DifferentMagnitudeUnitsError
    return value*iu.factor/ou.factor


# -------------------- Category ----------------------------

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = ProductCategory
    form_class = CategoryCreateForm
    template_name = 'utils/category_create.html'
    success_url = reverse_lazy('list-category')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductCategory
    form_class = CategoryCreateForm
    template_name = 'utils/category_create.html'
    success_url = reverse_lazy('list-category')


class CategoryListView(LoginRequiredMixin, ListView):
    model = ProductCategory
    template_name = 'utils/category_list.html'


@login_required
def delete_category(request, id):
    # fetch the object related to passed id
    category = get_object_or_404(ProductCategory, id=id)
    category.delete()
    return redirect('list-category')


# -------------------- Order ----------------------------

@login_required
def create_order(request, provider_id, product_id=None):
    if product_id:
        product = get_object_or_404(Product, id=product_id)
        last_purchase = ProductTransaction.objects.filter(order__type='purchase',
                                                          product=product).order_by('-id').first()
        if last_purchase:
            last_provider = last_purchase.order.associated
            # Search for a pending order from the same provider
            pending_order = Order.objects.filter(associated=last_provider,
                                                 status='pending').first()
            if pending_order:
                return redirect('create-transaction', pending_order.id, product_id)

        # Create new order from the
        return redirect('create-transaction-new-order', product_id)
    else:
        provider = get_object_or_404(Associated, id=provider_id)
        # request.session.get('associated_id')
        initial = {'associated': provider}
        form = OrderCreateForm(initial=initial)
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.type = 'purchase'
                order.created_by = request.user
                order.save()
                return redirect('detail-order', id=order.id)
        context = {
            'form': form
        }
        return render(request, 'inventory/order_create.html', context)


@login_required
def select_provider(request):
    associateds = Associated.objects.filter(
        type='provider', active=True).order_by("-created_date")
    return render(request, 'inventory/provider_list.html', {'associateds': associateds})


@login_required
def update_order(request, id):
    # fetch the object related to passed id
    obj = get_object_or_404(Order, id=id)

    # pass the object as instance in form
    form = OrderCreateForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        order = form.save()
        return redirect('detail-order', id=order.id)

    # add form dictionary to context
    context = {
        'form': form
    }

    return render(request, 'inventory/order_create.html', context)


@login_required
def update_order_status(request, id, status):
    order = get_object_or_404(Order, id=id)
    order.status = status
    order.save()
    if status == 'complete':
        transactions = ProductTransaction.objects.filter(order=order)
        for transaction in transactions:
            handle_transaction(transaction, order)
        return redirect('list-order')
    else:
        return redirect('detail-order', id=order.id)


@login_required
def list_order(request):
    orders = Order.objects.filter(
        type='purchase').order_by('-created_date')
    statuses = set()
    for order in orders:
        statuses.add(order.status)
        transactions = ProductTransaction.objects.filter(order=order)
        amount = 0
        for transaction in transactions:
            amount += getTransactionAmount(transaction)
        order.amount = amount
    return render(request, 'inventory/order_list.html', {'orders': orders,
                                                         'statuses': statuses})


@login_required
def detail_order(request, id):
    order = Order.objects.get(id=id)
    transactions = ProductTransaction.objects.filter(order=order)
    # Compute amount
    amount = 0
    for transaction in transactions:
        transaction.amount = transaction.quantity * \
            transaction.price*(1 + transaction.tax/100.)
        amount += transaction.amount
    order.amount = amount
    # Order by amount
    transactions = list(transactions)
    transactions.sort(key=lambda trans: trans.amount, reverse=True)
    # Terminated order
    terminated = order.status in ['decline', 'complete']
    empty = len(transactions) == 0
    return render(request, 'inventory/order_detail.html', {'order': order,
                                                           'transactions': transactions,
                                                           'terminated': terminated,
                                                           'empty': empty})


# -------------------- Transaction ----------------------------

def getNewOrder(associated: Associated, product: Product):
    return Order.objects.create(concept="Restock of {}".format(product.name),
                                note="Automatically created for the purchase of product {}. Please, check all details!".format(
        product.name),
        type='purchase',
        associated=associated)


def renderCreateTransaction(request, form, product, order_id):
    context = {
        'form': form,
        'product': product,
        'order_id': order_id,
        'title': _("Create Transaction")
    }
    return render(request, 'inventory/transaction_create.html', context)


@login_required
def create_transaction(request, order_id, product_id):
    order = Order.objects.get(id=order_id)
    product = Product.objects.get(id=product_id)
    form = TransactionCreateForm(initial={'unit': product.unit})
    if request.method == 'POST':
        form = TransactionCreateForm(request.POST)
        if form.is_valid():
            trans = form.save(commit=False)
            trans.order = order
            trans.product = product
            trans.save()
            return redirect('detail-order', id=order_id)
    return renderCreateTransaction(request, form, product, order_id)


@login_required
def create_transaction_new_order(request, product_id):
    product = Product.objects.get(id=product_id)
    initial = {'unit': product.unit,
               'created_by': request.session.get('associated_id')}
    last_purchase = ProductTransaction.objects.filter(order__type='purchase',
                                                      product=product).order_by('-id').first()
    order_id = -1
    if last_purchase:
        form = TransactionCreateForm(initial=initial)
    else:
        form = TransactionProviderCreateForm(initial=initial)
    if request.method == 'POST':
        if last_purchase:
            form = TransactionCreateForm(request.POST)
        else:
            form = TransactionProviderCreateForm(request.POST)
        if form.is_valid():
            if last_purchase:
                last_provider = last_purchase.order.associated
            else:
                last_provider = form.cleaned_data['associated']

            order = getNewOrder(last_provider, product)
            trans = form.save(commit=False)
            trans.order = order
            trans.product = product
            trans.save()
            return redirect('detail-order', id=order.id)
    return renderCreateTransaction(request, form, product, order_id)


@login_required
def update_transaction(request, id):
    # fetch the object related to passed id
    transaction = get_object_or_404(ProductTransaction, id=id)

    # pass the object as instance in form
    form = TransactionCreateForm(request.POST or None,
                                 instance=transaction)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('detail-order', id=transaction.order.id)

    # add form dictionary to context
    context = {
        'form': form,
        'product': transaction.product,
        'order_id': transaction.order.id,
        'title': _("Update Transaction")
    }

    return render(request, 'inventory/transaction_create.html', context)


@login_required
def detail_transaction(request, id):
    # fetch the object related to passed id
    transaction = get_object_or_404(ProductTransaction, id=id)
    return render(request, 'inventory/transaction_detail.html', {'transaction': transaction,
                                                                 'amount': getTransactionAmount(transaction)})


def getTransactionAmount(transaction: ProductTransaction):
    return transaction.quantity * \
        transaction.price*(1 + transaction.tax/100.)


def handle_transaction(transaction: ProductTransaction, order: Order):
    #  To be performed on complete orders
    product = transaction.product
    # To be used in the rest of the system
    product = Product.objects.get(id=product.id)
    product_quantity = convertUnit(
        input_unit=transaction.unit,
        output_unit=product.unit,
        value=transaction.quantity)

    # TODO study taxes handling on sales to improve these formula
    # Generate stock
    cost = transaction.price*(1 + transaction.tax/100.)  # Add on taxes
    Stock.objects.create(product=product,
                         quantity=product_quantity,
                         cost=cost)
    product.quantity += product_quantity
    product.stock_price += product_quantity * cost
    product.save()


@login_required
def delete_transaction(request, id):
    # fetch the object related to passed id
    transaction = get_object_or_404(ProductTransaction, id=id)
    transaction.delete()
    return redirect('detail-order', id=transaction.order.id)


# -------------------- Unit ----------------------------


@login_required
def create_unit(request):
    form = UnitCreateForm()
    if request.method == 'POST':
        form = UnitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-unit')
    context = {
        'form': form
    }
    return render(request, 'inventory/unit_create.html', context)


@login_required
def update_unit(request, id):
    # fetch the object related to passed id
    unit = get_object_or_404(Unit, id=id)

    # pass the object as instance in form
    form = UnitCreateForm(request.POST or None,
                          instance=unit)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('list-unit')

    # add form dictionary to context
    context = {
        'form': form,
    }

    return render(request, 'inventory/unit_update.html', context)


@login_required
def list_unit(request):
    units = Unit.objects.all()
    return render(request, 'inventory/unit_list.html', {'units': units})


@login_required
def delete_unit(request, id):
    # fetch the object related to passed id
    unit = get_object_or_404(Unit, id=id)
    unit.delete()
    return redirect('list-unit')


# -------------------- Product ----------------------------

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'inventory/product_create.html'
    success_url = reverse_lazy('list-product')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'inventory/product_create.html'
    success_url = reverse_lazy('list-product')


def product_list_metadata(type, products: List[Product]):
    category_names = []
    categories = []
    alerts = 0
    for product in products:
        if product.type == type:
            # Average cost
            product.average_cost = 0
            if product.quantity > 0:
                product.average_cost = product.stock_price/product.quantity
            product.sell_price = product.average_cost * \
                (1 + product.suggested_price/100)
            # Categories
            if product.category.name not in category_names:
                category_names.append(product.category.name)
                categories.append(product.category)
            # Alerts
            if product.quantity < product.quantity_min:
                alerts += 1
    return (categories, alerts)


def prepare_product_list():
    products = Product.objects.all()
    (consumable_categories, consumable_alerts) = product_list_metadata(
        'consumable', products)
    (part_categories, part_alerts) = product_list_metadata('part', products)

    return {'products': products,
            'consumable_alerts': consumable_alerts,
            'consumable_categories': consumable_categories,
            'part_alerts': part_alerts,
            'part_categories': part_categories}


@login_required
def list_product(request):
    response = prepare_product_list()
    return render(request, 'inventory/product_list.html', response)


@login_required
def select_product(request, next, order_id):
    response = prepare_product_list()
    response.setdefault("next", next)
    response.setdefault("order_id", order_id)
    return render(request, 'inventory/product_select.html', response)


@login_required
def select_new_product(request, next, order_id):
    form = ProductCreateForm()
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect(next, order_id=order_id, product_id=product.id)
    context = {
        'form': form,
        'next': next,
        'order_id': order_id,
    }
    return render(request, 'inventory/product_create.html', context)


@login_required
def detail_product(request, id):
    # fetch the object related to passed id
    product = get_object_or_404(Product, id=id)
    product.average_cost = 0
    if product.quantity > 0:
        product.average_cost = product.stock_price/product.quantity
    product.sell_price = product.average_cost * \
        (1 + product.suggested_price/100)
    product.sell_max = product.average_cost * \
        (1 + product.max_price/100)

    stocks = Stock.objects.filter(product=product).order_by('-created_date')
    purchases = ProductTransaction.objects.filter(
        product=product, order__type='purchase',
        order__status='complete').order_by('-order__created_date')
    latest_purchase = purchases.first()
    latest_order = None
    if latest_purchase:
        latest_order = latest_purchase.order
    return render(request, 'inventory/product_detail.html', {'product': product,
                                                             'stocks': stocks,
                                                             'purchases': purchases,
                                                             'latest_order': latest_order})


@login_required
def delete_product(request, id):
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id=id)
    obj.delete()
    return redirect('list-product')
