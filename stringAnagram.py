def stringAnagram(input_list):
    def helper(string):
        total = 0
        
        for each_char in string:
            total += 101 ** (ord(each_char) - ord('a'))
        
        return total
        
    all_val, all_strings = dict(), []
    
    for word in input_list:
        val = helper(word)
        
        if val in all_val:
            all_val[val].append(word)
        
        else:
            all_val[val] = [word]
    
    for key, value in all_val.items():
        all_strings.append(value)
    
    return all_strings
    
print(stringAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

print(stringAnagram([""]))
# Output: [['']]

print(stringAnagram(["a"]))
# Output: [['a']]