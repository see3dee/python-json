import json

json_file = open("/home/see3dee/src/python-json/movie_1.txt", "r", encoding="utf-8")
movie_dict = json.load(json_file)
json_file.close()
print(movie_dict['is_awesome'])
print(f" movie_dict is of type: {type(movie_dict)}")
print(movie_dict.keys())
print(movie_dict.values())
print(movie_dict.items())
print(sorted(movie_dict.keys()))
## Common case -- loop over the keys in sorted order,
## accessing each key/value
for key in sorted(movie_dict.keys()):
    print(key, movie_dict[key])