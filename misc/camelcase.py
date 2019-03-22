import sys
import re        

# https://www.hackerrank.com/challenges/camelcase

# input
s = input().strip()
# find number of 'words' starting with capital letter
w = re.findall('[A-Z][a-z]*', s)
# add one more for the word starting the string with lower case letter
out = len(w) + 1
print(out)
        
        
        
        
    
    
    
    
     
    