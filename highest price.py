def best_stock(data):
    max_price = 0
    answer = ''
    for s in data:
        if data[s] > max_price:
            max_price = data[s]
            answer = s
    return answer

xx={'CAC': 10.0,'ATX': 390.2,'WIG': 400}
print (best_stock(xx))
