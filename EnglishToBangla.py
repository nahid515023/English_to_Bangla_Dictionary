def main():
    chack = input("\nEnter the word : ")
    word = chack_word(chack)
    print('\n<--------------------------------------------------------------->')
    print(f'\n\t\t{chack} --> {word}')
    print('\n<--------------------------------------------------------------->\n')


def chack_word(chack):
    file = 'BengaliDictionary_17 copy.txt'
    try:
        with open(file, 'r', encoding='utf-8') as file:
            for line in file:
                if chack in line:
                    count = 0
                    l = len(chack)
                    for i in range(l):
                        if chack[i] == line[i+1]:
                            count += 1
                    if count == l and line[i+2] == '|':
                        return possesing(line)
        return 'The word is not found.'
    except FileNotFoundError:
        print('No such file or directory?')


def possesing(word):
    l = ''
    for i in word:
        if i > "|":
            l += i
    return l


if __name__ == '__main__':
    main()
