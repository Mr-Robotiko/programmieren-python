import itertools
from typing import List


def print_dna_combination():
    DNA: List[str] = ["AT", "TA", "GC", "CG"]
    DNA_combinations: itertools.combinations_with_replacement = itertools.combinations_with_replacement(DNA, 4)
    print("======== ALLE SEQUENZEN ================")
    for i in DNA_combinations:
        print(i)
    print("========================================")


if __name__ == '__main__':
    print_dna_combination()