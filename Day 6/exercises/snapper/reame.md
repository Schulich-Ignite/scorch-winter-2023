# Snapper



Snapper is a new social media company that lets you post pictures. For now you have been asked to hook up the backend to the user page.

People will search by an id number to find users to see their profile and posts



**Layout**:

- /templates/user.html is the template you will use want to render the user page

- routes.py contains all the routes and will be where you start the server from: *python routes.py*

- models.py doesn't need to be touched, but contains the class definitions

**Data structure**:
The classes are:




```python
class Post:
    title: str
    description: str
    image: str

class User:
    name: str
    banner: str
    image: str
    bio: str
    posts: List[Post]
```



- Inside routes.py the users variable is a list of users, when you create your route, the ID will be the index of the user you want to access (or subtract 1)
  **Remember indices start at 0 & make sure your test id is in range!**



So go and:

1. Create a `/user/<id_number>` route (never use `id` it's reserved in python)

2. Use the data to load in /templates/user.html



You can test by running python routes.py and then go to your browser and type in [http://localhost:5000](http://localhost:5000)


