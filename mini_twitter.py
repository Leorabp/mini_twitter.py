users = {}        # usernames will go here
posts = []        # every post you create gets added here
post_id = 1       # each post gets its own number


def create_user():
    print ("write your username here")
    username = input()
    print(f'{username} nice to meet you!')
    bio = input("bio: ")

    if username in users:
        print("That username already exists.")
        return None

    users[username] = {
        "bio": bio,
        "followers": 0,
        "posts": []
}
    
    print (f"Thank you for writing your username, {username}. You can now access twitter. Look below to view your profile")
    return username


def create_post(username):
    global post_id

    if not username:
        print("no user signed in")
        return

    post_text = input("please write a post:")

    post = {
        "id": post_id,
        "user": username,
        "text": post_text,
        "likes": 0
        
    }

    posts.append(post)
    users[username]["posts"].append(post)
    
    print ("Post saved!! Wonderful job!")
    post_id+= 1

def view_posts():
        if not posts:
            print ("No posts yet:(")
            return

        for post in posts:
            print(f'{post["user"]}: {post["text"]} - Likes: {post["likes"]}')

username = create_user()

if username:
    create_post(username)
    view_posts()

while True:
    print("\nMenu:")
    print("1. Create a user")
    print("2. Write a post!")
    print("3. View your feed!")
    print("4. Like some posts")
    print("5. Exit twitter")

    choice = input("Choose an option: ")

    if choice == "1":
        current_user = create_user()
    elif choice == "2":
        if current_user:
            create_post(current_user)
        else:
            print("You must create a user first!")
    elif choice == "3":
        view_posts()
    elif choice == "4":
        like_post()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try Again please!")
            



def like_post():
    try:
        pid = int(input("Enter the post ID to like: "))
    except ValueError:
        print("No. Please enter a valid number.")
        return

    for post in posts:
        if post["id"] == pid:
            post["likes"] += 1
            print("Yay! Post liked!")
            return
        print("Post ID not found...")
