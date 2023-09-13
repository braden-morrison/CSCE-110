import string
import os

try:
    val = True
    with open('sentences.txt', 'x') as f:
        while val:
            sentence = input("Enter a sentence: ")
            if sentence == 'quit':
                break

            puncs = '''!()-[]{};:'"\,<>./?@#$%^&*~'''
            sentence2 = " "

            for i in sentence:
                if i not in puncs:
                    sentence2 += i
            s = sentence2.split()[::-1]
            l = []
            for i in s:
                l.append(i.upper())
            f.write(" ".join(l))
            f.write('\n')
    f.close()
except FileExistsError:
    val = True
    with open('sentences.txt', 'w') as f:
        while val:
            sentence = input("Enter a sentence: ")
            if sentence == 'quit':
                break

            puncs = '''!()-[]{};:'"\,<>./?@#$%^&*~'''
            sentence2 = " "

            for i in sentence:
                if i not in puncs:
                    sentence2 += i
            s = sentence2.split()[::-1]
            l = []
            for i in s:
                l.append(i.upper())
            f.write(" ".join(l))
            f.write('\n')
    f.close()
