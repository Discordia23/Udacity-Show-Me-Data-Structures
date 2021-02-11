"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def callFromBangalore(num):
    if num[0][:5] == '(080)':
        return num

def callToBangalore(num):
    if num[1][:5] == '(080)':
        return num

def mobileCalled(num):
    if call[1][0] != '(':
        return num

def codeFixedLine(num):
    code_fixedLine = ''
    for digit in call[1]: # loop through the digits of called number until the closing parenthese
        code_fixedLine += digit
        if digit == ')':
            break
    return code_fixedLine

lst = []
callsFromBengalore = 0
callsFromAndToBangalore = 0
for call in calls:
    if callFromBangalore(call): # if calling number is from Bangalore
        callsFromBengalore += 1 # count calls for question part B
        if mobileCalled(call): # if the called number is a mobile phone, append the code (first 4 digits) to lst
            lst.append(call[1][:4])
        else: # if the called number is a fixed line, append the code (digits in parentheses) to lst. Calls to telemarketers are not existing
            lst.append(codeFixedLine(call))
    if callFromBangalore(call) and callToBangalore(call): # if calling number and called number are both from Bangalore
        callsFromAndToBangalore += 1 # count calls for question part B

result = sorted(set(lst)) # remove duplicated codes through set() and sort the remaining codes

print("The numbers called by people in Bangalore have codes:")
for code in result:
    print(code)

print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(callsFromAndToBangalore/callsFromBengalore))
