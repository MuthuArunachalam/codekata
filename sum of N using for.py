n=int(input("Enter the number:"))
if n<0:
      print("Enter a positive number")
else:
    sum=0
    for i in range (0,n+1):
        sum +=i
print(sum) 
