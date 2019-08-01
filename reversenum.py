#reverse the two digits number

n = input("Enter a Number : ")
#print(len(n))
num=int(n)
tot = 0
temp = 0
while num != 0:
    temp = num % 10
    tot = (tot*10) + temp
    num = num // 10
print("Reverse =",tot)
if int(n) == tot:
    print("Palindrome")
else:
    print("not palindrome")
