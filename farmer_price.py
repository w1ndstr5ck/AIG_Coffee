price_per_contract = 4.00
order_qnt = 5
sale_price = 37.46
farmer_prob = 0.5

def price(price_per_contract, order_qnt, seller_price, farmer_prob):
    total_value = price_per_contract / farmer_prob
    item_spread = total_value / order_qnt
    offer_price = seller_price - item_spread
    return offer_price

print(price(price_per_contract, order_qnt, sale_price, farmer_prob))