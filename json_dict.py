import json
# Dealing with json packets in files
# open file with json packets as json_file
json_file = open("/home/see3dee/src/python-json/movie_1.json", "r", encoding="utf-8")

# use json.load method to convert the json into python dictionary movie_dict
movie_dict = json.load(json_file)
json_file.close()
print(f" movie_dict is of type: {type(movie_dict)}")
# navigate the dictionary using methods keys, values and items
print(movie_dict['is_awesome'])
print(movie_dict.keys())
print(movie_dict.values())
print(movie_dict.items())
print(sorted(movie_dict.keys()))
print(f"{movie_dict['title']} was released in the year {movie_dict['release_year']}")

# Common case -- loop over the keys in sorted order,
# accessing each key/value
for key in sorted(movie_dict.keys()):
    print(key, movie_dict[key])

# Let's convert the dictionary into a json-packet in a file object, using the json.dump method
# first create a new file object 'txt_file_json' with the open function
txt_file_json = open("/home/see3dee/movie.txt", "w", )
json.dump(movie_dict, txt_file_json)
# see output file: /home/see3dee/movie.txt


# Dealing with json packets in strings
# json packet in triple quotes
json_string = """{
    "title": "Gattaca",
    "release_year": 1997,
    "is_awesome": true,
    "won_oscar": false,
    "actors": ["Ethan Hawke", "Uma Thurman", "Alan Arkin", "Loren Dean"],
    "budget": null,
    "credits": {
        "director": "Andrew Niccol",
        "writer": "Andrew Niccol",
        "composer": "Michael Nyman",
        "cinematographer": "Slawomir Idziak"
    }
}"""

# use the json.loads method to create python dictionary; movie_dict
movie_dict = json.loads(json_string)

print(f" movie_dict is of type: {type(movie_dict)}")
# navigate the dictionary using methods keys, values and items
print(movie_dict['is_awesome'])
print(movie_dict.keys())
print(movie_dict.values())
print(movie_dict.items())
print(sorted(movie_dict.keys()))
print(f"{movie_dict['title']} was released in the year {movie_dict['release_year']}")

# Common case -- loop over the keys in sorted order,
# accessing each key/value
for key in sorted(movie_dict.keys()):
    print(key, movie_dict[key])

# Let's convert the dictionary back to a json-packet string, using the json.dumps method

json_packet = json.dumps(movie_dict)
print(f" here is the json packet using the json.dumps() on the movie_dict: {json_packet}")
