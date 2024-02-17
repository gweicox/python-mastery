
with open("Data/portfolio.dat") as f:
    data = f.read().strip()
    data = [line.split()[1:] for line in data.splitlines()]
    res = sum(int(row[0]) * float(row[1]) for row in data)

print(res)
