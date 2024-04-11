

def getBondPrice_E(face, couponRate, m, yc):
    bondPrice = 0
    coupon = face * couponRate  # This is the annual coupon payment
    for t, y in enumerate(yc, start=1):
        if t != m:
            bondPrice += coupon / ((1 + y)**t)
        else:
            bondPrice += (coupon + face) / ((1 + y)**t)
    return bondPrice

