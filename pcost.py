
def portfolio_cost(filename):
    with open(filename, "r") as f:
        data = f.read().strip().splitlines()
        acc = 0
        for line in data:
            ticker, number, price = line.split()
            try:
                number, price = int(number), float(price)
                acc += number * price
            except ValueError as e:
                print(f"Couldn't parse: {line}\nReason: {e}")
    return acc

print(portfolio_cost('Data/portfolio3.dat'))
