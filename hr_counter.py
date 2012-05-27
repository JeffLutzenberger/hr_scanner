 #!/usr/bin/python
import re

def mapper(file, phrases):
    results = []
    violators = []
    for line in file:
        for p in phrases:
            if line.find(p) > 0 and line.find('***') < 0:
                results.append((p,1))
                v = line.partition('] ')[2].partition(':')[0]
                violators.append((v,1))
    return results, violators

def Reduce(mappings):
    results = []
    for k, v in mappings.iteritems():
        results.append((k, reduce( lambda x, y: x+y, v )))
    return results

def Partition(L):
    tf = {}
    for p in L:
        try:
            tf[p[0]].append (1)
        except KeyError:
            tf[p[0]] = [1]
    return tf

def tuple_sort (a, b):
  if a[1] < b[1]:
    return 1
  elif a[1] > b[1]:
    return -1
  else:
    return cmp(a[0], b[0])

#read phrases
phrase_file = open('phrases.txt', 'r')
phrases = []
print("reading phrase file...\r\n")
for line in phrase_file:
    phrases.append(line.rstrip())
phrase_file.close()
#print phrases

#read in transcript and match phrases
transcript_file = open('ta_chat_room_3_months.log', 'r')
print("scanning chat room transcript for hr violations...\r\n")

words, violators =  mapper(transcript_file, phrases)
transcript_file.close()
words = Reduce(Partition(words))
violators = Reduce(Partition(violators))

words.sort(tuple_sort)
violators.sort(tuple_sort)
    
#print("found " + str(hr_violations) + " hr violations:")
print "\r\n*** HR Violations ***\r"
for w in words:
    print w[0] + " " + str(w[1])

print "\r\n*** Violators ***\r"
for v in violators:
    print v[0] + " " + str(v[1])
    


        