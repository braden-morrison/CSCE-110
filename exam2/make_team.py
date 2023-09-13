# make_team.py
import random


def main():
    string = input("Enter the student names: ").split(",")
    n = input("Enter the team size: ")
    print()
    if len(string) < int(n):
        print('The team size is too large.')
    else:
        list = make_team(string, n)
        print('The team is: ', end="")
        for x in list:
            if x == list[len(list)-1]:
                print(x,end="")
            else:
                print(x, end=",")


def make_team(names, team_size):
    list2 = random.choices(names, k = int(team_size))
    return list2

    

if __name__ == '__main__':
    main()