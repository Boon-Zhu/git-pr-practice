def login(username, password):
    if username == "admin" and password == "123456":
        return True
    return False


if __name__ == "__main__":
    print(login("admin", "123456"))
    