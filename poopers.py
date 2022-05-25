#extract floating point number from end of the string
# assume there is a colon before the number

str = 'X-DSPAM-Confidence: 0.8475'

# step 1: find the position of the colon
colon = str.find(':')
# step 2: use slicing to extract the string following the colon
slice = str[colon+1:]
# step 3: convert to a floating point number

val = float(slice)

print('Extracted value: ', val)
