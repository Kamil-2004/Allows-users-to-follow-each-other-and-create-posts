logo = """

 ▄▄▄·      .▄▄ · ▄▄▄▄▄
▐█ ▄█▪     ▐█ ▀. •██  
 ██▀· ▄█▀▄ ▄▀▀▀█▄ ▐█.▪
▐█▪·•▐█▌.▐▌▐█▄▪▐█ ▐█▌·
.▀    ▀█▄▀▪ ▀▀▀▀  ▀▀▀ 

"""
print(logo)

class User:
    def __init__(self, username):
        self.username = username
        self.following = set()
        self.posts = []

    def follow(self, other_user):
        if other_user != self:
            self.following.add(other_user)
            print(f"{self.username} now follows {other_user.username}")

    def unfollow(self, other_user):
        if other_user in self.following:
            self.following.remove(other_user)
            print(f"{self.username} has unfollowed {other_user.username}")

    def create_post(self, content):
        post = Post(self, content)
        self.posts.append(post)
        print(f"{self.username} created a new post: {content}")

    def __str__(self):
        return f"User: {self.username}"


class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.likes = set()

    def like(self, user):
        if user != self.author:
            self.likes.add(user)
            print(f"{user.username} liked a post by {self.author.username}")

    def __str__(self):
        return f"Post by {self.author.username}: {self.content} | Likes: {len(self.likes)}"


class SocialNetwork:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"Added new user: {user.username}")

    def show_all_users(self):
        print("Users in the social network:")
        for user in self.users:
            print(user)

    def show_user_posts(self, user):
        print(f"Posts by {user.username}:")
        for post in user.posts:
            print(post)


# Example usage
if __name__ == "__main__":
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
