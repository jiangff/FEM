## FEM




##----- find related videos ----------------------------

import json
import re
import numpy

query = json.loads(open('C:/video_tag.json').read())
v = query

##------ compare text similarity ---------------------------

##def levenshtein(s1, s2):
##    if len(s1) < len(s2):
##        return levenshtein(s2, s1)
## 
##    # len(s1) >= len(s2)
##    if len(s2) == 0:
##        return len(s1)
## 
##    previous_row = xrange(len(s2) + 1)
##    for i, c1 in enumerate(s1):
##        current_row = [i + 1]
##        for j, c2 in enumerate(s2):
##            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
##            deletions = current_row[j] + 1       # than s2
##            substitutions = previous_row[j] + (c1 != c2)
##            current_row.append(min(insertions, deletions, substitutions))
##        previous_row = current_row
## 
##    return previous_row[-1]

##print levenshtein('dog','cat')

## --- count tag number ------------

def tag_compare(l1,l2):

    count = 0
    for x in l1:
        if x in l2:
            count = count + 1

    return count

## ---- count numer of the same words ----

def word_number(l1,l2):

    x = l1.split()
    y = l2.split()

    count = 0
    for word in x:
        if word in y:
            count = count +1

    return count

print word_number('i like pizza','pizza is good!')

## ---- code ----------------

for m in range(len(query)):

    similarity = []
     
    for n in range(len(query)):

        N_tag = tag_compare(query[m]['tag'],query[n]['tag'])
        N_title = word_number( query[m]['title'],query[n]['title'] )
        N_description = word_number( query[m]['description'],query[n]['description'] )
            
        similarity.append( N_tag + N_title/25.0 + N_description/50.0)

    related = numpy.argsort(similarity)
    
    v[m]['related-1'] = query[related[-2]]['title']
    v[m]['related-2'] = query[related[-3]]['title']
    v[m]['related-3'] = query[related[-4]]['title']
                        
    print m
    print related[-1]
                        
##---- import query into a json file -----------------

f =open('C:/video_related.json','w')

for line in v:

    del( line['categories'] )
    json.dump(line,f,indent=3)
    f.write(',\n')
    
f.close()








    


