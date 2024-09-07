# Social Network Simulator

A simple Python program to simulate a social network with users, posts, and likes.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Classes and Methods](#classes-and-methods)
5. [Example Usage](#example-usage)

## Features

* Create users and add them to the social network
* Users can follow each other
* Users can create posts
* Users can like posts created by other users
* Display all users in the social network
* Display posts created by a specific user

## Installation

To run this program, you need to have Python installed on your system. You can download the latest version of Python from the official Python website.

## Usage

1. Clone the repository or download the `social_network.py` file.
2. Run the program using Python: `python social_network.py`

## Classes and Methods

### User Class

* `__init__(username)`: Initializes a new user with the given username.
* `follow(other_user)`: Makes the current user follow the given user.
* `unfollow(other_user)`: Makes the current user unfollow the given user.
* `create_post(content)`: Creates a new post with the given content.
* `__str__()`: Returns a string representation of the user.

### Post Class

* `__init__(author, content)`: Initializes a new post with the given author and content.
* `like(user)`: Makes the given user like the post.
* `__str__()`: Returns a string representation of the post.

### SocialNetwork Class

* `__init__()`: Initializes a new social network.
* `add_user(user)`: Adds the given user to the social network.
* `show_all_users()`: Displays all users in the social network.
* `show_user_posts(user)`: Displays all posts created by the given user.

## Example Usage

```python
# Create a social network
sn = SocialNetwork()

# Create users
Kamil = User("Kamil")
Ahad = User("Ahad")
Ibrahim = User("Ibrahim")

# Add users to the network
sn.add_user(Kamil)
sn.add_user(Ahad)
sn.add_user(Ibrahim)

# Users follow each other
Kamil.follow(Ahad)
Ahad.follow(Ibrahim)

# Users create posts
Kamil.create_post("Hello World!")
Ahad.create_post("Python is great!")
Ibrahim.create_post("Excited to join the network!")

# Users like posts
Ahad.posts[0].like(Ibrahim)
Ibrahim.posts[0].like(Kamil)

# Show all users
sn.show_all_users()

# Show posts by a specific user
sn.show_user_posts(Ahad)
