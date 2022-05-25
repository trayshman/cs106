#Ryan Jones
#Assignment 2

age=input('Enter your age as an integer: ') #gets variable input for age
try:
    x=int(age) #checks to make sure integer was entered
except:
    print('Not correct value, setting age to 35.')
    age=35 #integer wasn't entered, system sets it as 35
credit=input('Enter your credit score as an integer: ') #gets variable input for credit score
try:
    x=int(credit) #checks to make sure integer was entered
except:
    print('Not correct value, setting credit score to 670')
    credit=670 #integer not entered, sets credit score to 670
traffic=input('Enter your number of traffic violations in the past 5 years: ') #gets variable input for number of traffic violations
try:
    x=int(traffic) #checks to make sure integer was entered
except:
    print('You did not enter an integer, setting traffic violations to 2.')
    traffic=2 #integer not entered, sets traffic violations to 2




if int(traffic)>=6:
    print('Insurance not offered by this company') #Automatically denies them insurance if 6 or more traffic incidences
else:
    if int(age)<25: #for customers under 25
        if int(credit)>700: #that have a credit score above 700
            insurance=2200 #traffic already defined as less than 6
        else: #credit score of 700 or below
            if int(traffic)<3:#with less than 3 traffic incidences
                insurance=2500
            else: #3, 4 or 5 traffic incidences
                insurance=3000
    else: #for customers 25 or older
        if int(credit)>700: #with a credit score above 700
            if int(traffic)<4: #with less than 4 traffic incidences
                insurance=800
            else: #with 4 or 5 traffic incidences
                insurance=1500
        else: #credit score of 700 or below
            if int(traffic)<4: #with less than 4 traffic incidences
                insurance=1200
            else: #with 4 or 5 traffic incidences
                insurance=2000


    print('Your annual premium is $',insurance)
