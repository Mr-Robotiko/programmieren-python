def checksum(isbn: str) -> int:
    sum: int = 0
    for i in range(1, len(isbn)):
        value: int = i * int(isbn[i-1])
        sum += value
    return sum % 11
