

txt = input("Enter Message: ")
n = 0
ones = 0
print( "You Entered: " + txt)
for i in range(0,len(txt)-1): 
    if txt[i] == "0" and txt[i+1] == "1":
        print("MATCH!")
        n += 1
    elif txt[i] == "1" and txt[i+1] == "1":
            print("ONE-@NE!")
            ones += 1
    i += 2
print("Total of 01 words: " + str(n) )
print("Total of ONES: " + str(ones) )

if ( n > 0 and ones == 2*n):
    print( "YES" )
else:
    print("NO")


