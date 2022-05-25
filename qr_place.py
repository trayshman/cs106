# qr_place.py
# Author: Christine F. Reilly
# This program prints what quantitative reasoning course a student may take

aqr = input('Does the student place into AQR? (enter y or n): ')

if aqr == 'y':
    print('The student may take an AQR or FQR course')
else:
    # We need more information to determine if the student can take FQR
    fqr = input('Does the student place into FQR? (enter y or n): ')

    if fqr == 'y':
        print('The student may take an FQR course')
    else:
        print('The student should take Math 100')

# After executing the block of code for the matching condition(s), the flow
# of control goes to the statment following the selection structure
print('Thank you for using the QR placement program!')
