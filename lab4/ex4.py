fl = 40
fh = 200
b = fh - fl

kmax = int(fh // b)
for k in range(kmax, 0, -1):
    fmin = 2 * fh / k
    fmax = 2 * fl / (k - 1) if k > 1 else float('inf')
    if fmin <= fmax:
        print(k, fmin)
        break
