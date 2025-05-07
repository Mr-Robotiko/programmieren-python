def wurzel(x: int, n: int = 10):
    i: int = 0.5*(n + x/n)
    if n > 0:
        n -= 1
        return wurzel(x, i)
    else:
        return 0


if __name__ == '__main__':
    n: int = 0
    print(wurzel(n))