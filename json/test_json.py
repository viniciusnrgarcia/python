import json
from pprint import pprint
from typing import TypedDict

# from dataclasses import dataclass, asdict, astuple

# @dataclass(init=True)


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


json_str = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
'''


# Conversão de json para python
print(json_str)

movie: Movie = json.loads(json_str)

pprint(type(movie))
pprint(movie)
print(movie['title'])
print(movie['year'])


# Conversão de python para json
print(json.dumps(movie, ensure_ascii=False, indent=2))

j = json.dumps(movie, ensure_ascii=False, indent=2)
print(j)  # str json
