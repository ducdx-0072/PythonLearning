# Letter Counter App
# This is a console app that:
# 1 - Allow users to enter a string
# 2 - Then allow users to enter a character or a string
# 3 - Prints the number of occurences of the character of string in (2) in the string in (1)
from collections import Counter
import re

src = input('Input a string: ')

char = ''

while char != 'q':
    char = input("Input a character or a string to count (q to quit): ")
    if char != 'q':
        # Count by api of string
        count = src.count(char,0)
        print("'", char, "' occurs ", count, " times - by string api")

        #Count by for loop 
        count = 0
        for c in src:
            if c == char:
                count += 1
        print("'", char, "' occurs ", count, " times - by for loop") 

        #Count by collections api 
        count = Counter(src)[char]
        print("'", char, "' occurs ", count, " times - by Counter of collection") 

        #Count by lambda 
        lamb = lambda str:1 if char in str else 0
        count = sum(map(lamb,src))
        print("'", char, "' occurs ", count, " times - by sum + map + lambda") 

        #Count by Regular Expression
        count = len(re.findall(char,src))
        print("'", char, "' occurs ", count, " times - by Regular Expression") 