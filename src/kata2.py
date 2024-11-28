"""
    author: Santiago Porollan
    email: santiago.porollan@gmail.com
"""
from src.kata1 import Dictionary


def get_total(costs, items, tax):
    # Get sum of costs:
    sum = 0
    for item in items:
        try:
            cost = costs.look(item)
            sum = sum + cost
        except TypeError:
            # ignore item that doesn't have cost
            pass

    # Add tax and return
    return round(sum * (1+tax), 2)


if __name__ == '__main__':
    costs = Dictionary()
    costs.newentry('socks', 5)
    costs.newentry('shoes', 60)
    costs.newentry('sweater', 30)
    total = get_total(costs, ['socks', 'shoes'], 0.09)

    # expected: 70.85
    print(total)
