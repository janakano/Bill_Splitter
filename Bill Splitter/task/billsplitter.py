import random
print("Enter the number of friends joining (including you):")
count = int(input())
total_friends = count
friends = {}

if count <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    while count > 0:
        names = input()
        count -= 1
        friends[names] = 0
    print("Enter the total bill value:")
    total = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == "Yes":
        new_list = list(friends.keys())
        lucky = random.choice(new_list)
        print(lucky + " is the lucky one!")
        split = round((total / (total_friends-1)),2)
        for friend in friends:
            friends[friend] = split
        friends[lucky] = 0
        print(friends)
    else:
        print("No one is going to be lucky")
        split = round((total / total_friends),2)
        for friend in friends:
            friends[friend] = split
        print(friends)
    