

def getBondPrice(y, face, couponRate, m, ppy=1):
    coupon_payment = face * couponRate / ppy
    bondPrice = 0

    for t in range(1, m * ppy + 1):
        bondPrice += coupon_payment / ((1 + y / ppy) ** t)

    bondPrice += face / ((1 + y / ppy) ** (m * ppy))
    return bondPrice
