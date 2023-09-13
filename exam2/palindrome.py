# palindrome.py

def main():
    """Driver function"""
    text = input(" Enter words: ")
    print('Palindrome booleans:', find_palindromes(text))
    print('Number of palindromes:', count_palindromes(find_palindromes(text)))


def find_palindromes(text):
    list = text.split()
    bool_list = []
    for x in list:
        if x == x[::-1]:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list
   

def count_palindromes(text):
    count = 0
    for x in text:
        if x == True:
            count+= 1
    return count


if __name__ == '__main__':
    main()