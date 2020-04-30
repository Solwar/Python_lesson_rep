def weather(temperature):
    if temperature < 0:
        return 'So cold'
    elif 0 <= temperature <= 15:
        return 'A little cold'
    elif 15 <= temperature <= 25:
        return 'A temperature is normal'
    else:
        return 'Hot!'


print(weather(5))