
from mylib import *

if __name__ == "__main__":
    N = int(1e6)
    hit = 0
    for _ in range(N):
        x, y = rand_point()
        if x * x + y * y <= 1:
            hit = hit + 1

    approx_pi = hit * 4 / N

    print(approx_pi)
    print(abs(approx_pi - pi))
    print(100 * abs(approx_pi - pi) / pi)
