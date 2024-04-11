
def getBondDuration(y, face, couponRate, m, ppy = 1):
    coupon = face * couponRate
    discounted_cash_flows = []
    for t in range(1, m+1):
        cash_flow = coupon + (face if t == m else 0)
        discounted_cash_flow = cash_flow / ((1 + y/ppy) ** t)
        discounted_cash_flows.append(discounted_cash_flow)
    duration = sum(t * dcf for t, dcf in enumerate(discounted_cash_flows, 1)) / sum(discounted_cash_flows)
    
    return duration
