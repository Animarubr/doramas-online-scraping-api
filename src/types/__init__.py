from typing import Dict, List
from json import dumps
from dataclasses import dataclass

@dataclass
class NewEpisodes:
    title: str
    thumbnail: str
    link: str
    episode: int
    season: int
    
@dataclass
class Cards:
    title: str
    thumbnail: str
    link: str
    year: int


@dataclass
class PlayerEpisode:
    title: str
    link: str

@dataclass
class Episodes:
    thubnail: str
    episode: int
    link: str
    season: int

@dataclass
class PageInfo:
    title: str
    thumbnail: str
    score: int
    votes: int
    genres: List[str]
    description: str
    episodes: Episodes

