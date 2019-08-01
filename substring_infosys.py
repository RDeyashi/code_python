#print the length of longest substring with no duplicate character.

from sys import stdin, stdout

def func(x):
    length = len(x)
    StrList = []
    if length >1:
        for i in range(length):
            num = ord(x[i])
            if num in StrList:
                return x[0:i]
            elif num  >= 65 and num < 91:
                StrList.append(num)
                StrList.append(num + 32)
            elif num >= 97 and num < 123:
                StrList.append(num)
                StrList.append(num - 32)
            else:
                StrList.append(num)
    else:
        return x

def myfunc(x):
    return len(x)

# driven program
stdout.write('Longest Substring without duplicate\n\nEnter a String')
Str = stdin.readline()
#STR = Str
#Str.upper()
L1 = len(Str)
mylist = []
for i in range(L1):
    result = func(Str[i:L1])
    if result == None:
        mylist.append(Str[i:L1])
    else:
        mylist.append(result)
#print(mylist)
mylist.sort(reverse=True, key=myfunc)
maxlen = len(mylist[0])
x=True
for i in mylist:
    if len(i) == maxlen and len(i) >=3:
        stdout.write(i)


