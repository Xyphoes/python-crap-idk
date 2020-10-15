Choice = str(input("SI for simple interest and CI for compound interest. Write in capital letters."))

Principal = int(input("Write your Principal"))
Rate = int(input("Write your rate of interest here."))
Time = int(input("Write your time period"))

if Choice == 'SI':
    print ((Principal * Rate * Time)/100)
elif Choice == 'CI':
    print(Principal*(1 + Rate/100)**(Time))
