def main():
    list1 = [2, 2, 3]
    list2 = [4, 5, 6]

    result = list(map(lambda a,b: a * b, list1, list2))
    print(result)


if __name__ == '__main__':
    main()