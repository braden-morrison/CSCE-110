
def main():
    """This function asks the user for the sides to roll, rolls the valid sides and prints the sum of all the valid
    sides rolled """
    # To do: write your code in this function
    
    choice = input("Command (roll or quit): ")
    if choice == 'quit':
        print('End of the game!')
    while choice != 'quit':
        if choice == 'roll':
            sides = input("Enter the sides to roll: ").split()
            total_sum = 0
            for side in sides:
                side = int(side)
                if side > 0 and side < 7:
                    total_sum += side
                    roll_die(side)
            print('The sum of the valid sides rolled is:', total_sum)
        print()
        choice = input("Command (roll or quit): ")
        if choice == 'quit':
            print('End of the game!')

  
    
        






# Do not write / modify anything below this line

def roll_die(value):
    """DO NOT MODIFY: This function takes a number between 1 and 6 as input and draws a die side with that number"""
    border = '+-------+'
    empty = '|       |'
    one_left = '| *     |'
    one_mid = '|   *   |'
    one_right = '|     * |'
    two = '| *   * |'
    three = '| * * * |'
    side1 = [border, empty, one_mid, empty, border]
    side2 = [border, one_left, empty, one_right, border]
    side3 = [border, one_left, one_mid, one_right, border]
    side4 = [border, two, empty, two, border]
    side5 = [border, two, one_mid, two, border]
    side6 = [border, three, empty, three, border]

    die = ['', side1, side2, side3, side4, side5, side6]

    for i in range(5):  # number of lines required to visualize a die
        print(die[value][i])


main()
