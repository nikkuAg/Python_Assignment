str = input()
str = str.lower()
new_str = ""
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
 
for i in str:
    if(i not in vowels):
        new_str = new_str + '.' + i
        
 
print(new_str)