# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if user1.get('valid', True):
            return fn(*args, **kwargs)
        else:
            return print("Not authorised")
    return wrapper


@authenticated
def message_friends(user):
    print(f"Message has been sent to {user['name']}")


(message_friends(user1))
