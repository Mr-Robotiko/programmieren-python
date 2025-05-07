def wurzel(x, n=10, z=1):
    if n == 0:
        return z
    else:
        step: int = 0.5 * (z + x / z)
        return wurzel(x, n - 1, step)


if __name__ == '__main__':
    n: int = 2
    print(wurzel(n))