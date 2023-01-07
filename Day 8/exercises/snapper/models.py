from dataclasses import dataclass
from typing import List

@dataclass
class Post:
    title: str
    description: str
    image: str

@dataclass
class User:
    name: str
    banner: str
    image: str
    bio: str
    posts: List[Post]
