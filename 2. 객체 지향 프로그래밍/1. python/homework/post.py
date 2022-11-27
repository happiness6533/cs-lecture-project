import csv

# 수업
def make_post(me, content):
    if me is None:
        return False

    file = open("posts.csv", "r", encoding="utf8")
    lines = file.readlines()

    next_post_id = 0
    if len(lines) > 0:
        next_post_id = int(lines[len(lines) - 1].strip().split(" ")[0]) + 1

    file = open("posts.txt", "a", encoding="utf8")
    file.write(f"{next_post_id + 1} {content} {me['id']}\n")
    file.close()


# 수업
def load_post(me):
    my_posts = []

    if me is None:
        return my_posts

    file = open("posts.txt", "r", encoding="utf8")

    lines = file.readlines()
    for line in lines:
        line_array = line.strip().split(" ")
        stored_id = line_array[0]
        stored_content = line_array[1]
        stored_user_id = line_array[2]
        if stored_user_id == me['id']:
            my_post = {
                "id": stored_id,
                "content": stored_content,
                "user_id": stored_user_id,
            }
            my_posts.append(my_post)

    return my_posts


# 퀴즈
def update_post():
    pass


# 퀴즈
def delete_post():
    pass
