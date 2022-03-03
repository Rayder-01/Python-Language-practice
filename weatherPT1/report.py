from random import choice


def get_description():
    """Retur random weather, just like the pros"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who kows']
    return choice(possibilities)
