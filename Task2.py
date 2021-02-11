"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

dct = {}
for call in calls:
    if call[0] not in dct:
        dct[call[0]] = int(call[-1])
    else:
        dct[call[0]] += int(call[-1])
    if call[1] not in dct:
        dct[call[1]] = int(call[-1])
    else:
        dct[call[1]] += int(call[-1])

longesttime = max(dct, key=lambda x: dct[x])

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longesttime, dct[longesttime]))
