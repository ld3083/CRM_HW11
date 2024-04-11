

def getBondPrice_Z(face, couponRate, times, yc):
    bondPrice = 0
    for t, y in zip(times, yc):
        discountFactor = 1 / ((1 + y) ** t)
        if t == times[-1]:
            coupon = face * couponRate
            bondPrice += (coupon + face) * discountFactor
        else:
            bondPrice += face * couponRate * discountFactor
    return (bondPrice)
