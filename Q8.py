month_name = input("Enter month name: ")
month_name = month_name.title()

first_6_month=['Farvardin','Ordibehesht','Khordad','Tir','Mordad','Shahrivar']
second_5_month=['Mehr','Aban','Azar','Dey','Bahman']

if month_name in first_6_month:
    print (31)
elif month_name in second_5_month:
    print(30)
elif month_name == 'Esfand':
    print(29)
else:
    print('incorect month name')