from sys import stdin, stdout
year= int(stdin.readline())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            stdout.write("%d is a Leap Year\n"% year)
        else:
            stdout.write("{} is not a Leap Year\n".format(year))
    else:
        stdout.write("{} is a Leap Year\n".format(year))
else:
    stdout.write("{} is not a Leap Year\n".format(year))




