month_name = input("Enter month name: ")
month_name = month_name.title()

first_3_month=['Farvardin','Ordibehesht','Khordad']
second_3_month=['Tir','Mordad','Shahrivar']
third_3_month=['Mehr','Aban','Azar']
fourth_3_month=['Dey','Bahman','Esfand']

if month_name in first_3_month:
    print ('spring')
elif month_name in second_3_month:
    print('summer')
elif month_name in third_3_month:
    print('fall')
elif month_name in fourth_3_month:
    print('winter')
else:
    print('incorect month name')