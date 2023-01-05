import spacy 
nlp = spacy.load('en_core_web_md')
#imported spaCy 

with open('T38/movies.txt', 'r+') as a: 
   movies = a.read()
# Imported movies.txt

movies = movies.split("\n")
#split movie text to create a list containing movies and descriptions 

Hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
#created variable Hulk with description

hulk_nlp = nlp(Hulk)
# made hulk npl function 

similarity_list = []
#created a list to include all the similarity score

def what_movie (movies, hulk_nlp):
# created function what_movie to find the most similar movie

    for movie in movies:
        similarity = nlp(movie).similarity(hulk_nlp)
        similarity_list.append(similarity) 
# checks for similarities in movies 

    movies_sim_list = dict()
# creates dictionary including movies and their respective similarity

    for item in range(len(movies)):
        key = movies[item]
        value = similarity_list[item]
        movies_sim_list[key] = value 
# creates for loop adding movies and similarity to dictionary

    most_sim = max(movies_sim_list, key=movies_sim_list.get)
# this finds the most similar movie by finding the max similar score

    most_sim = most_sim.split(":")
    print(f"The most similar movie is {most_sim[0]} and the description is: {most_sim[1]}")
# this splits the most similar movie so it can be printed and then prints

what_movie(movies, hulk_nlp)
# calls function 