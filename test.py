# group anagrams 
from collections import defaultdict 
mapp= defaultdict(list) 
strs = ["act","pots","tops","cat","stop","hat"]
for word in strs : 
    count =[0]*26
    print(f"count : {count}")
    for c in word: 
        count[ord(c) - ord('a')]+=1 
    print(f"count : {count}, word : {word }")
    mapp[tuple(count)].append(word) 
    
print(mapp ) 
ans = []
for y in mapp.values(): 
    ans.append(y)
print(f"ans : {ans}")
# return ans 