
def repeater(initial: str):
    value = initial
    while True:
        new = yield value
        if new is not None:
            value = new


if __name__ == '__main__':
    rep = repeater("DHBW-Mannheim")
    print(next(rep))
    print(rep.send("DHBW-Eppelheim"))
    print(next(rep))