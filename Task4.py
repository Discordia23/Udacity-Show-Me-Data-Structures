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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

calling_numbers = set()
called_numbers = set()
texting_numbers = set()
texted_numbers = set()

for call in calls:
    calling_numbers.add(call[0])
    called_numbers.add(call[1])

for text in texts:
    texting_numbers.add(text[0])
    texted_numbers.add(text[1])

telemarketers = calling_numbers - called_numbers - texting_numbers - texted_numbers

print("These numbers could be telemarketers: ")
for num in sorted(telemarketers):
    print(num)
