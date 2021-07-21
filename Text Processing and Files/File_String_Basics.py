#port.py

total = 0.0
with open('portfolio.csv', 'r') as f:
    headers = next(f)       # Skip a sin;e line of input
    for line in f:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        parts[3] = float(parts[3])
        total += parts[2]*parts[3]

print('Total cost', total)
