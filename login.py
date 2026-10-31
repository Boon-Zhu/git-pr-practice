def login(username, password):
    if not username or not password:
        return {
            "success": False,
            "message": "Username and password are required"
        }

    if username == "admin" and password == "123456":
        return {
            "success": True,
            "message": "Hello! You have logged in successfully."
        }

    return {
        "success": False,
        "message": "Invalid credentials"
    }


if __name__ == "__main__":
    print(login("admin", "123456"))