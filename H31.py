from heapq import heappush, heappop, heapify
from collections import defaultdict
 

 
def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()] # за всяка вероятност създава [[wt, [sym, ""]]  
    heapify(heap) # обръщаме масив в дърво
    while len(heap) > 1:
        lo = heappop(heap) # вземаме най-малък елемент от дървото и го премахаме от там 
        hi = heappop(heap)
        for pair in lo[1:]: # обозночаваме за лява - 0 ва стойност
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1] # обозночаваме за дясна - 1 на стойност
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:]) # събираме вероятности и връщаме в дървото
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]),p) ) # сортираме по дължина на кода връщаме ['А','001'] 
 
def huffmanDecode (dictionary, text):
    res = ""
    while text:
        for k in dictionary:
            if text.startswith(str(k[1])):
                res += str(k[0])
                text = text[len(str(k[1])):]
    return res

txt = "Hello"
#txt = input("Enter Message: ")

symb2freq = defaultdict(int) # Създаваме Речник 
for ch in txt:
    symb2freq[ch] += 1 #Намираме вероятности

huff = encode(symb2freq)
print ("Char\tWeight\tCode")
for p in huff:
    print ("%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1]))

stringed = ""
for ch in txt:
    for p in huff:
        if p[0] == ch:
            stringed= stringed + p[1]

print(stringed)
print( huffmanDecode(huff, stringed))
