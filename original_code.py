# original_code.py

class O:
    def __init__(self, n, p, q):
        self.n = n
        self.p = p
        self.q = q


def calc(o):
    t = 0
    if o.q > 0:
        t = o.p * o.q
    else:
        t = 0

    if t > 100:
        t = t * 0.9
    else:
        t = t

    return t


def process(orders):
    res = []
    for i in range(len(orders)):
        o = orders[i]
        if o is not None:
            total = calc(o)
            print("Order:", o.n, "Total:", total)
            res.append(total)
    return res