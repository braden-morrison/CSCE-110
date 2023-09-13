# get_price program

def main():
    """Driver function. Do not modify this function."""
    basket1 = {"Lemon": 1.25, "Apple": 0.50, "Orange": 8.75, "Mango": 2, "Papaya": 4.60, "Kiwi": 3}
    basket2 = {"Guava": 4, "Grapes": 9.25, "Pear": 6, "Cherry": 2.99}
    print(f"The most expensive fruit in basket 1 is: {get_price(basket1)}")
    print(f"The most expensive fruit in basket 2 is: {get_price(basket2)}")


def get_price(fruits):
    max = 0.00
    max_key = ''
    for x, y in fruits.items():
        if y > max:
            max = y
            max_key = x
    return max_key
    
    


if __name__ == '__main__':
    main()