def div(a, b):
    if not isinstance(a, float) and not isinstance(a, int):
        return 'a and b must both be float or integer.'
    if not isinstance(b, float) and not isinstance(b, int):
        return 'a and b must both be float or integer.'
    if a > 0 and b == 0:
        return 'Inf'
    elif a < 0 and b == 0:
        return '-Inf'
    elif a ==0 and b == 0:
        return 'NaN'
    else:
        return a/b


def add(a, b):
    if not isinstance(a, float) and not isinstance(a, int):
        return 'a and b must both be float or integer.'
    if not isinstance(b, float) and not isinstance(b, int):
        return 'a and b must both be float or integer.'
    return a + b
