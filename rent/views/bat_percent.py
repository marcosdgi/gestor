charge_state = {
    3.00: 0,
    3.01: 0,
    3.02: 0,
    3.03: 0,
    3.04: 0,
    3.05: 0,
    3.06: 0,
    3.07: 0,
    3.08: 0,
    3.09: 0,
    3.10: 1,
    3.11: 1,
    3.12: 1,
    3.13: 1,
    3.14: 1,
    3.15: 1,
    3.16: 1,
    3.17: 1,
    3.18: 1,
    3.19: 2,
    3.20: 2,
    3.21: 2,
    3.22: 2,
    3.23: 2,
    3.24: 2,
    3.25: 2,
    3.26: 2,
    3.27: 2,
    3.28: 3,
    3.29: 3,
    3.30: 3,
    3.31: 3,
    3.32: 3,
    3.33: 3,
    3.34: 3,
    3.35: 3,
    3.36: 3,
    3.37: 4,
    3.38: 4,
    3.39: 4,
    3.40: 4,
    3.41: 4,
    3.42: 4,
    3.43: 4,
    3.44: 4,
    3.45: 4,
    3.46: 5,
    3.47: 5,
    3.48: 5,
    3.49: 5,
    3.50: 6,
    3.51: 6,
    3.52: 6,
    3.53: 6,
    3.54: 6,
    3.55: 7,
    3.56: 7,
    3.57: 7,
    3.58: 7,
    3.59: 8,
    3.60: 8,
    3.61: 8,
    3.62: 8,
    3.63: 8,
    3.64: 9,
    3.65: 9,
    3.66: 9,
    3.67: 9,
    3.68: 9,
    3.69: 11,
    3.70: 13,
    3.71: 14,
    3.72: 16,
    3.73: 18,
    3.74: 19,
    3.75: 23,
    3.76: 26,
    3.77: 29,
    3.78: 34,
    3.79: 39,
    3.80: 43,
    3.81: 46,
    3.82: 49,
    3.83: 51,
    3.84: 53,
    3.85: 55,
    3.86: 57,
    3.87: 59,
    3.88: 61,
    3.89: 63,
    3.90: 65,
    3.91: 67,
    3.92: 69,
    3.93: 71,
    3.94: 73,
    3.95: 74,
    3.96: 76,
    3.97: 78,
    3.98: 79,
    3.99: 81,
    4.00: 82,
    4.01: 83,
    4.02: 84,
    4.03: 86,
    4.04: 87,
    4.05: 88,
    4.06: 89,
    4.07: 90,
    4.08: 91,
    4.09: 92,
    4.10: 92,
    4.11: 93,
    4.12: 94,
    4.13: 94,
    4.14: 95,
    4.15: 96,
    4.16: 97,
    4.17: 97,
    4.18: 98,
    4.19: 99}


def vbat2percent(vbat):
    if vbat < 3:
        return 0
    if vbat > 4.19:
        return 100
    return int(charge_state[int(vbat*100)/100])