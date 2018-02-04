

#word = input("Enter Word:")
word = "ababab"
count = 0

def checkForWord( position, counter ):
    if word[position] == 'b'and word[position+1] == 'a' and word[position+2] == 'b' :
        counter += 1
        return checkForWord(position+2, counter)
    else:
        print("IN")
        return position

if (len(word)%3) == 0 and len(word) != 0 :
    print("Can be a word")
    try:
        i=0
        for i in range(0, len(word)-2, 3):
            if word[i] == 'a'and word[i+1] == 'b' and word[i+2] == 'a' :
                print("aba")
                i = checkForWord( i+2, count)
            else:
                print("not a word")
                break
    except ValueError:
        print("ERROR")
else:
    print("Definetly not a word")

