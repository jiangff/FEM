FEM
===

Tag videos and find related videos

                         Summary of coding assignment
                                                          
                                                      Feifei Jiang

Tag videos:

 I retrieved actors/actresses, TV shows, films from DPpedia using the SNORQL explorer http://dbpedia.org/snorql/, by inputting command lines as follows: 

(1) 
SELECT ?actress WHERE { ?actress <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:American_film_actresses> }

This automatically generates a .json file that contains a list of actress in the category American_film_actress in Wikipedia. Same for actors.

 (2)
SELECT ?television WHERE { ?television <http://purl.org/dc/terms/subject> <http://dbpedia.org/resource/Category:2000s_American_television_series> }

This generates a .json file that contains a list of US TV shows, and same for films.

At the end, I obtain several .json files with a  list of  TV shows, movies, actors using the method above. Then I search the title and description of each video in the given .json file and tag keywords from my list to that video.


Find related Videos:

I define the similarity between video x and video y as

Similarity = N_tag (x,y) + N_title(x,y)/25 + N_description(x,y)/50

N_tag(x,y) is the number of tags that y shares with x,
N_title(x,y) shows how similar the titles of 2 videos are. It is the number of distinct words that exist in both the “titles” of x and y;
N_description(x,y) shows how similar descriptions of 2 videos are. It is the number of distinct words that exist in both the “description” of x and y.

Because tags are much more important than just a random word in the title, and title is in general more important than descriptions in determining what the video is about, I assign weight 1, 1/25, and 1/50 so that N_tag is the primary factor that determines how related two videos are, and N_title and N_description are the 2nd and 3rd factors.  The larger the similarity values, the more related a video is to the target video.


Output:

For each video x, I search through the list using the algorithm above and locate videos with the 4 largest similarity values. The video with the largest similarity value is x itself, and the rest are the 3 most related videos. 

In the output video_related.json file, the title, description, tag and 3 related videos are listed:
“related-3” is the 3rd most related video
“related-2” is the 2nd most related video
“related-1” is the most related video

Attached are also the tag.py (tag videos) and related.py (find related videos).
