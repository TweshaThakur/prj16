#program to calculate the number of days you since you have been born

def mdaycalc(d,m):
    mo={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    a=0
    c=1
    for i in mo:
        if c==m:
            break
        c+=1
        a+=mo[i]
    return a+d


    
def nday(d,e):
    day1,month1,year1=d
    day2,month2,year2=e
    t1=(day1,month1,year1)
    t2=(day2,month2,year2)

    #general approach --> no. of days in birth year+ no. of dyas in current year + no. of leap years + 365* years in between
    
    ntoday=mdaycalc(day1,month1)
    ndate=365-mdaycalc(day2,month2)
    ly=(year1-year2)//4
    
    nday=(year1-1-year2)*365+ntoday+ndate+ly
    
    print("no. of days You have been alive: ",nday)



a=input("Enter your birth date(DD/MM/YYYY): ").split("/")
bdate=[int(i) for i in a]
b=input("Enter today's date(DD/MM/YYYY): ").split("/")
tdate=[int(i) for i in b]
nday(tdate,bdate)



    
