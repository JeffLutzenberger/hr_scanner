#!/usr/bin/python
import re

#read phrases
phrase_file = open('phrases.txt', 'r')
phrases = []
print("reading phrase file...\r\n")
for line in phrase_file:
    phrases.append(line.rstrip())
phrase_file.close()

print phrases

snitch = ['hr_violation','hr_violations']

violators = {}

#read in transcript and match phrases
transcript_file = open('ta_chat_room_3_months.log', 'r')
print("scanning chat room transcript for hr violations...\r\n")
hr_violations = 0
for line in transcript_file:
    line = line.lower()
    #print line
    for p in phrases:
        if line.find(p) > 0 and line.find('***') < 0:
            hr_violations += 1
            #print line
            v = line.partition(']')[2].partition(':')[0]
            if not v in violators:
                violators[v] = 1
            else:
                violators[v] += 1
            break
transcript_file.close()
print("found " + str(hr_violations) + " hr violations:")
for k, v in violators.iteritems():
    print k, v
