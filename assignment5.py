#Name: Ryan Jones

#fname = 'alb_weather_jan2020.txt' #test file
fname = 'alb_weather_2020.txt' #initialize the file

f_read=open(fname) #open the file

minDate=None #will be used to store the date that the minimum minimum temp was found on
maxDate=None #will be used to store the date that the maximum maximum temp was found on
count=0 #the total number of average weather temps
total=0 #the total amount of average weather temps added together
tempMin=None #used to store the minimum minimum temp
tempMax=None #used to store the maximum maximum temp
minCount=0 #counter for how many times the minimum minimum temperature shows up
maxCount=0 #counter for how many times the maximum maximum temperature shows up

for line in f_read: #for every line in the text file
    good_line=line.strip() #blank spaces gone

    if good_line.startswith('GHCND'): #ignore the headers of the text file
        parts=good_line.split() #tokenize


        tempAv = parts[10] #location of the average temp
        avTempAv = int(tempAv) #initialize as integer
        total+=avTempAv #add it to the total
        count+=1 #count goes up by one per weather temp

        ptempMin = parts[12] #location of the min temp
        intTempMin = int(ptempMin) #initialize as integer
        if tempMin is None or intTempMin < tempMin: #if there is no value for tempMin, or if this new value is less than all of the previous ones
            tempMin=intTempMin #it's assigned to the minimum minimum temp variable
            minDate=parts[6] #locates the section of the line where the date is
            minCount=0 #resets the minCount to zero
        if intTempMin == tempMin: #if that minimum minimum temperature shows up again
            minCount+=1 #the counter goes up by 1
        ptempMax = parts[11] #location of the max temp
        intTempMax = int(ptempMax) #initialize as integer
        if tempMax is None or intTempMax > tempMax: #if there is no value for tempMax, or if this new value is greater than all of the previous ones
            tempMax=intTempMax #it gets assigned to the maximum maximum temp variable
            maxDate=parts[6] #location where the date is
            maxCount=0 #resets minCount to zero
        if intTempMax == tempMax: #if that maximum maximum temp shows up again
            maxCount+=1 #counter goes up by 1
average = total/count #the total of the average temps divided by the number of average temps

minYear=minDate[0:4] #the year from that minDate
minMonth=minDate[4:6] #the month from that minDate
minDay=minDate[6:] #the day from that minDate


maxYear=maxDate[0:4] #the year from that maxDate
maxMonth=maxDate[4:6] #the month from that maxDate
maxDay=maxDate[6:] #the day from that maxDate

print('Average of the daily average temperature readings:','%.3f' % (average)) #displays the average of the average temps to 3 numbers after the decimal
print('The minimum temperature was',tempMin,'first seen on',minMonth+'/'+minDay+'/'+minYear,'and was recorded',minCount,'times') #displays the minimum minimum temp, where it was first seen on, and how many times it showed up in the text file
print('The maximum temperature was',tempMax,'first seen on',maxMonth+'/'+maxDay+'/'+maxYear,'and was recorded',maxCount,'times') #displays the maximum maximum temp, where it was first seen on, and how many times it showed up in the text file
