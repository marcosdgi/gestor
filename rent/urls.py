from django.urls import path
from .views import vehicle, tracker, lease, calendar, client, invoice
from django.views.generic import TemplateView
from .permissions import staff_required_view
from .views.cost  import (
    # ---- Category -------
    CategoryListView,
    delete_category,
    CategoryUpdateView,
    CategoryCreateView,
    # ---- Costs ----------
    create_cost,
    update_cost,
    list_cost,
    delete_cost,
    detail_cost
)
urlpatterns = [
    # -------------------- Category ----------------------------
    path('create-category/', CategoryCreateView.as_view(),
         name='create-costs-rental-category'),
    path('update-category/<pk>', CategoryUpdateView.as_view(),
         name='update-costs-rental-category'),
    path('list-category/', CategoryListView.as_view(), name='list-costs-rental-category'),
    path('delete-category/<id>', delete_category, name='delete-costs-rental-category'),
    # -------------------- Costs ----------------------------
    path('create-cost/', create_cost, name='create-cost-rental'),
    path('update-cost/<id>', update_cost, name='update-cost-rental'),
    path('list-cost/', list_cost, name='list-cost-rental'),
    path('list-cost/<year>/<month>', list_cost, name='list-cost-rental'),
    path('detail-cost/<id>', detail_cost, name='detail-cost-rental'),
    path('delete-cost/<id>', delete_cost, name='delete-cost-rental'),
    # -------------------- Vehicle ----------------------------
    path('create-trailer', vehicle.create_trailer, name='create-trailer'),
    path('list-trailer', vehicle.list_equipment, name='list-trailer'),
    path('select-trailer', vehicle.select_trailer, name='select-trailer'),
    path('update-trailer/<id>', vehicle.update_trailer, name='update-trailer'),
    path('delete-trailer/<id>', vehicle.delete_trailer, name='delete-trailer'),
    path('detail-trailer/<id>', vehicle.detail_trailer, name='detail-trailer'),
    path('select-towit', vehicle.select_towit, name='select-towit'),
    # -------------------- Tracker ----------------------------
    path('create-tracker/<int:trailer_id>',
         tracker.TrackerCreateView.as_view(), name='create-trailer-tracker'),
    path('create-tracker/',
         tracker.TrackerCreateView.as_view(), name='create-tracker'),
    path('update-tracker/<slug:pk>',
         tracker.TrackerUpdateView.as_view(), name='update-tracker'),
    path('delete-tracker/<int:id>',  tracker.delete_tracker, name='delete-tracker'),
    path('detail-tracker/<int:id>',  tracker.tracker_detail, name='detail-tracker'),
    path('trackers-map/',  tracker.trackers, name='trackers-map'),
    path('trackers/',  tracker.trackers_table, name='trackers-table'),
    path('tracker-upload', tracker.tracker_upload, name='tracker-upload'),
    # -------------------- Manufacturer ----------------------------
    path('manufacturer-list', vehicle.manufacturer_list, name='manufacturer-list'),
    path('manufacturer-create/', vehicle.manufacturer_create,
         name='manufacturer-create'),
    path('manufacturer-update/<int:pk>',
         vehicle.manufacturer_update, name='manufacturer-update'),
    path('manufacturer-delete/<int:pk>',
         vehicle.manufacturer_delete, name='manufacturer-delete'),
    # -------------------- Picture ----------------------------
    path('picture/create/<int:trailer_id>',
         vehicle.trailer_picture_create, name='trailer-picture-create'),
    path('share_pictures/<ids>',  vehicle.share_pictures, name='share-pictures'),
    path('delete_trailer_pictures/<ids>',
         vehicle.delete_trailer_pictures, name='delete-trailer-pictures'),
    path('update_pinned_picture/<int:pk>/',
         vehicle.update_pinned_picture, name='update-pinned-picture'),
    # -------------------- Trailer Document ----------------------------
    path('document/create/<int:trailer_id>',
         vehicle.create_document, name='trailer-document-create'),
    path('update_trailer_document/<id>',
         vehicle.update_document, name='update-trailer-document'),
    path('delete_trailer_document/<id>',
         vehicle.delete_document, name='delete-trailer-document'),
    # -------------------- Contracts ----------------------------
    path('create_contract/<int:lessee_id>/<int:trailer_id>/',
         lease.contract_create_view, name='create-contract'),
    path('contract/<int:id>',  lease.contract_detail, name='detail-contract'),
    path('contract_signing/<int:id>',
         lease.contract_signing, name='contract-signing'),
    path('contract_pdf/<int:id>',  lease.contract_pdf,
         name='contract-signed'),
    path('contracts/',  lease.contracts, name='contracts'),
    path('update_contract/<slug:pk>',
         lease.ContractUpdateView.as_view(), name='update-contract'),
    path('update_contract_stage/<slug:id>/<stage>',
         lease.update_contract_stage, name='update-contract-stage'),
    path('capture_signature/<lease_id>/<position>',
         lease.create_handwriting, name='capture-signature'),
    path('capture_signature/<lease_id>/<position>/<external>',
         lease.create_handwriting, name='capture-signature'),
    # -------------------- Lessee ----------------------------
    path('select_lessee/<int:trailer_id>/',
         lease.select_lessee, name='select-lessee'),
    path('update_lesee/<int:trailer_id>/<int:lessee_id>/',
         lease.update_lessee, name='update-lessee'),
    path('create_lesee/<int:trailer_id>/',
         lease.update_lessee, name='create-lessee'),
    path('create_lessee_data/<int:trailer_id>/<int:lessee_id>/',
         lease.create_lessee_data, name='update-lessee-data'),
    path('update_lessee_data/<slug:pk>',
         lease.LeseeDataUpdateView.as_view(), name='update-lessee-data'),
    # -------------------- Inspection ----------------------------
    path('create_inspection/<lease_id>/',
         lease.create_inspection, name='create-inspection'),
    path('update_inspection/<id>/',
         lease.update_inspection, name='update-inspection'),
    path('update_tires/<inspection_id>/',
         lease.update_tires, name='update-tires'),
    # -------------------- Calendar ----------------------------
    path('api_occurrences/', calendar.api_occurrences, name='api-occurrences'),
    path('calendar/', calendar.calendar_week,  name='calendar'),
    # -------------------- Client ----------------------------
    path('toggle_alarm/<lease_id>/', client.toggle_alarm, name='toggle-alarm'),
    path('client_detail/<id>/', client.client_detail, name='client-detail'),
    path('client_list/', client.client_list, name='client-list'),
    path('client-garbage/<id>', client.client_ended_garbage, name='client-garbage'),
    path('payment/<client_id>/', client.payment, name='rental-payment'),
    path('detail_payment/<id>/', client.detail_payment, name='detail-payment'),
    path('revert_payment/<id>',
         client.revert_payment, name='revert-payment'),
    # -------------------- Invoice ----------------------------
    path('invoice/<lease_id>/<date>/<str:paid>',
         invoice.invoice, name='rental-invoice'),
    path('pdf-invoice/<lease_id>/<date>/<str:paid>',
         invoice.generate_invoice, name='rental-pdf-invoice'),
    path('send_mail/<lease_id>/<date>/<str:paid>',
         invoice.send_invoice, name='rental-send-invoice'),
    # -------------------- Lease Document ----------------------------
    path('lease_document/create/<int:lease_id>',
         lease.create_document, name='lease-document-create'),
    path('update_lease_document/<id>',
         lease.update_document, name='update-lease-document'),
    path('delete_lease_document/<id>',
         lease.delete_document, name='delete-lease-document'),
    # -------------------- Lease Deposit ----------------------------
    path('lease_deposit/create/<int:lease_id>',
         lease.create_deposit, name='lease-deposit-create'),
    path('delete_lease_deposit/<id>',
         lease.delete_deposit, name='delete-lease-deposit'),
    # -------------------- Lease ----------------------------
    path('update_lease/<id>',
         lease.update_lease, name='update-lease'),
    # -------------------- Due ----------------------------
    path('create_due/<int:lease_id>/<str:date>',
         lease.create_due, name='create-due'),
    path('update_due/<id>',
         lease.update_due, name='update-due'),
    # -------------------- Permissions ----------------------------
    path('staff_required/', staff_required_view, name='staff_required'),
     # -------------------- Cost ----------------------------
]
