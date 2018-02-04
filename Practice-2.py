

word = input("Enter Word:")



if (len(word)%3) == 0 and len(word) != 0 :
    print("Can be a word")
    try:
        i=0
        for i in range(0, len(word)-2, 3):
            if word[i] == 'a'and word[i+1] == 'b' and word[i+2] == 'a' :
                print("aba")
            else:
                print("not a word")
    except ValueError:
        print("ERROR")
else:
    print("Definetly not a word")
