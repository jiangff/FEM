
import json
import re


                  
##--------- tag video with keywords --------------------

data = json.loads(open('C:/youtube.json').read())
query = data

movie_list = open('C:/movie.dat','r')
movie = movie_list.readlines()
movie_list.close()

tv_list = open('C:/tv.dat','r')
tv = tv_list.readlines()
tv_list.close()

video = movie + tv
show = []

for j in range(len(video)):

    item = video[j]
    index = item.find('(')

    if index>0:
        video[j] = item[0:(index-1)]
    else:
        video[j] = item[:-1]
      
for item in video:
    if item not in show:
        show.append(item)
    
  
actor_list = open('C:/actors.dat','r')
actor = actor_list.readlines()
actor_list.close()

name_list=[]
k=0

for k in range(len(data)):

    entry = data[k]['title'] + ' '+ data[k]['description']

##----search movies and TVs and tag-----------------
  
    for item in show:

        if len(item) >= 3:

            match = re.search(r'\b'+ item +r'\b',entry)
            match_u = re.search(r'\b'+ item.upper() + r'\b',entry)
            match_l = re.search(r'\b'+ item.lower() + r'\b',entry)
      
        else:
            match = 0
            match_u = 0
            match_l = 0
    
        if match or match_u or match_l:
            name_list.append(item)
             
## ----search actors and tag ---------------------------
    
    for j in range(len(actor)):

        item = actor[j]
        index=item.find('(')

        if index>0:
            name = item[0:(index-1)]
        else:
            name = item[:-1]

        if len(name) >= 2:
   
            match = re.search(r'\b'+name+r'\b',entry)
            match_u = re.search(r'\b' + name.upper() + r'\b',entry)
            match_l = re.search(r'\b' + name.lower() + r'\b',entry)
        
        else:
            match = 0
            match_u = 0
            match_l = 0


        if match or match_u or match_l:
            name_list.append(name)
        

    query[k]['tag']=name_list
    
    print k
    print query[k]['tag']

    name_list=[]



##---- import query into a json file -----------------


f =open('C:/video_tag.json','w')

for line in query:

    json.dump(line,f,indent=2)
    f.write(',\n')

f.close()










