file = open("inputText.txt", "r")
file_content = file.read()

inputs = file_content.split() 
file = file.close()
#print(inputs)
nums = ['0','1','2','3','4','5','6','7','8','9']
keyNums = []
for line in inputs: 
  value = []
  
  for i in line: 
    if i in nums: 
      if value == []:
        value.append(i) 
        value.append(' ')

      #print(f"This {value[1]} is val[1]")
      value[1] = i 
  print(value)
  keyNums.append(''.join(value))
print(', '.join(keyNums)) 

total = 0
for i in keyNums: 
  total += int(i) 

print("Total: ", total)
