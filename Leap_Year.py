year=eval(input("enter the year:"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("{} it is a leap year.".format(year))
        else:
            print("{} it is not leap year.".format(year))
    else:
        print("{} it is a leap year".format(year))
else:
    print("{} it is not a leap year".format(year))
