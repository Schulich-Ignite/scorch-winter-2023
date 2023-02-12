`Instapic` is a new social media platform that allows users to share their images and experiences with the world. Whether it's a beautiful landscape, a delicious meal, or a special moment with friends and family, `Instapic` provides users with a platform to show off these memories with their followers. With a focus on visual storytelling, users can post images and add descriptions to give context and provide a deeper understanding of the story they are trying to tell.

In addition to sharing images and descriptions, `Instapic` also includes features such as the ability to post regular text posts. The platform also features a clean and intuitive user interface that makes it easy for users to navigate and interact with the content on the platform. Whether you're a seasoned social media user or new to the space, `Instapic` provides a unique and enjoyable experience for all.

## Deliverables

To get full points you only have to complete all of the levels. They build on top of each other as you go.

For all 3 levels use the code in `starter.py` to start.

### Level 1

Create the user profile page. This page should:

- Take in a username and find the corresponding user (i.e. `localhost:5000/user/@descent098` should get the user with descent098 as username)
- Parse the data of a user including:
  - Username
  - Real name
  - Profile picture
  - Bio
  - List of posts
    - Post picture (if it has one)
    - Post title
    - Post description

The starter code is available at `/templates/user.jinja`, and the starter function can be found in `routes.py` and is called `profile_page()`

### Level 2

Create a discover page. This page should:

- List all users and give you links to their profiles
- Create a "topic" link for different topics. When people click on the link they should only get the profiles with those topics specified

Before you can do this you will need to create a "topics" field for each user that is an array of items.

### Level 3

Create an account pages, and create post pages:

- Create an account page where people sign up with:
  - a **unique** username
  - A name
  - Topics 
  - profile picture
  - Bio
- A page to create posts
  - Optional image
  - Description
