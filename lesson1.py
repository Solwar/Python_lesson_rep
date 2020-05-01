def weather(temperature):
    if temperature < 0:
        return 'So cold'
    elif 0 <= temperature <= 15:
        return 'A little cold'
    elif 15 <= temperature <= 25:
        return 'A temperature is normal'
    else:
        return 'Hot!'

def discounted(price, discount, max_discount=20, name=''):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or "iphone" in name.lower():
        return price
    else:
        return price - (price * discount / 100)

print(discounted(50000, 10, name='OPPO'))

#print(weather(5))