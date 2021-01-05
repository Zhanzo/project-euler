def main(stop_year):
    num_sundays = calc_sundays(stop_year)
    print(num_sundays)

def calc_sundays(stop_year):
    num_sundays = 0
    day = 2
    month = 1
    year = 1901
    date = 1
    while (year < stop_year):
        if (day == 7 and date == 1):
            num_sundays += 1
            
        if (day == 7):
            day = 1
        else:
            day += 1
        

        if (month == 2 and year % 4 != 0 and date == 28):
            month += 1
            date = 1
        elif (month == 2 and year % 4 == 0 and date == 29):
            month += 1
            date = 1
        elif ((month == 4 or month == 6 or month == 9 or month == 11) and date == 30):
            month += 1
            date = 1
        elif ((month == 1 or month == 3 or month == 5 or month == 7 
                        or month == 8 or month == 10) and date == 31):
            month += 1
            date = 1
        elif (month == 12 and date == 31):
            year += 1
            month = 1
            date = 1
            print(year)
        else:
            date += 1
    return num_sundays
        
main(2001)
