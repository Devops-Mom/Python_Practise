# Create a list of your friends' names and now create a list of tuples.
# The tuple should contain the friend’s name and the length of the name.
# For Example: if someone’s name is Aditya, the tuple would be: (‘Aditya’, 6)

def friend_collection(name):
    length = len(name)

    return name, length


friends = []
frd_tuple = []
flag = 'y'
while flag == 'y':
    n = input('Enter name of your friend: ')
    friends.append(n)
    frd_tuple.append(friend_collection(n))
    flag = input("Do you have more friends to add, if 'yes' enter 'y'")


if flag != 'y':
    # frd_tuple = tuple(frd_tuple)
    print(f"Here, is your friend's name collection with their name length \n {frd_tuple}")
