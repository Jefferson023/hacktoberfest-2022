def sortList(lst: list) -> list:
    """Sorts a list of numbers in ascending order"""
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

if __name__ == "__main__":
    lst = []
    for i in range(3):
        lst.append(int(input("Digite um numero: ")))
    print(sortList(lst))