# jubayer-source github
# jubayer_source username list


def evencheck(n):
  
  even = []
  
  for ev in n:
    if ev % 2 == 0:
      even.append(ev)
    
  return even

number = [1,2,3,4,5,6,7,8]
print("Even number list : ",evencheck(number))


################ another approach

numbers = [1,2,3,4,5,6]
evenNumber = [num for num in numbers if num % 2 == 0]

print(f"TheEven number list :", evenNumber)
