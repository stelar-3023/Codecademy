# username_generator
def username_generator(first_name, last_name):
    username = first_name[:3] + last_name[:4]
    # return username
    print(username)

def password_generator(username):
    password = ""
    for i in range(len(username)):
        password += username[i-1]
    # return password
    print(password)


username_generator("Steve", "Larsen")
password_generator("SteLars")