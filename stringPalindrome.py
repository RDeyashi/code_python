from sys import stdin, stdout

def check(x,y):
    if x == y:
        return True
    else:
        return False

n = input("Enter a string : ")
Str = n.lower()
length = len(Str)
StrList=[]
for i in range(length):
    StrList.append(ord(Str[i])) #ord() to return the integer value of a character
revlist = StrList.copy()        #to copy the list
revlist.reverse()               #to reverse the list

for i in range(length):
    res = check(StrList[i],revlist[i])  #to check the both list of integer value is same or not
if res == True:
    stdout.write(n+" Is a Palindrome\n")
else:
    stdout.write(n+" Is not a Palindrome\n")
