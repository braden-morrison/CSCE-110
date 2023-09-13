
def main():
    """Driver function"""
    numbers = []
    numbers = input("Enter numbers: ").split()
    numbers = accumulate(numbers)
    print('Accumulated sum: ', end="")
    for x in numbers:
            if x == numbers[len(numbers)-1]:
                print(x)
            else:
                print(x, end=" ")


def accumulate(entries):
    """Returns a list of the accumulating sum"""
    list = []
    y = 0
    for x in entries:
        num = int(x)
        if y == 0:
            list.append(num)
        else:
            list.append(num + int(list[y - 1]))
        y += 1
    return list


if __name__ == '__main__':
    main()