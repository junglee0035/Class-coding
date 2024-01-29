def calcWeeklyWages(totalHours, hourlyWage):
    if totalHours <= 40:
        regularHours = totalHours
        overtime = 0
        doubletime = 0
    elif totalHours > 40 and totalHours <= 60:
        overtime = totalHours - 40
        regularHours = 40
        doubletime = 0
    elif totalHours > 60:
        doubletime = totalHours - 60
        overtime = totalHours - 40 - doubletime
        regularHours = 40
    return hourlyWage*regularHours + 1.5*hourlyWage*overtime + (2*hourlyWage)*doubletime

def main():
    hours = float(input('Enter hours worked: '))
    wage = float(input('Enter dollars paid per hour: '))
    total = calcWeeklyWages(hours, wage)
    print('Wages for {hours} hours at ${wage:.2f} per hour are ${total:.2f}.'
          .format(**locals()))

main()
