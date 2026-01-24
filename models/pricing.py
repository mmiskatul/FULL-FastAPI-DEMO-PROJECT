def reprice(cost, competitor_prices, min_margin=0.2):
    min_price = cost * (1 + min_margin)
    target_price = min(competitor_prices)
    return round(max(min_price, target_price), 2)
