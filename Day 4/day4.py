def authorize(username):
    authorized_users = ["user1", "user2", "user3"]

    # Decorator
    def auth_decorator(func):
        # Wrapper function that will be returned by the decorator function and will be executed instead of the original function
        def wrapper():
            if username in authorized_users:
                print(f"Executing function: {func.__name__}")
                func()
            else:
                print("Error: User is not authorized.")
        return wrapper

    return auth_decorator

@authorize("user4") # This will return the decorator function and will be executed with the function below 
def access_granted():
    print("Access granted!")

access_granted()