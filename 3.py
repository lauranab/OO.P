


def is_year_leap(year):
    if ((year%4 ==0) and (year%100 !=0) or (year%400 ==0)):
        print(True ,':',year,'is a leap year')

    else:
        print(False ,':',year,'is not a leap year') 
    return f"{year}"        
year=int(input('enter year: '))

is_year_leap(year)