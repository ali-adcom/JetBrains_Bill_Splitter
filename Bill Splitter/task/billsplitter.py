import random

friends_count = int(input('Enter the number of friends joining (including you):\n'))
names_list = []

if friends_count > 0:
    print('\nEnter the name of every friend (including you), each on a new line:')
    for _ in range(friends_count):  # show input for each friend's name
        names_list.append(input())  # add friend's name ti names_list

    total_bill = int(input('\nEnter the total bill value:\n'))
    split_value = total_bill / friends_count  # split the bill among every friend
    split_value = round(split_value, 2)  # round the result of split amount for each friend to 2 decimal places

    joining_dict = dict.fromkeys(names_list, split_value)  # create a dict that contains the names as keys
    # (all values = the result of splitting the bill)

    print()
    
    lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    
    if lucky_feature == 'Yes':
        lucky_one = random.choice(list(joining_dict.keys()))
        print(f'\n{lucky_one} is the lucky one!\n')
        
        for friend in joining_dict:
            if friend == lucky_one:
                joining_dict[friend] = 0
                continue
            joining_dict[friend] = round(total_bill / (friends_count - 1), 2)
                
        print(joining_dict)
        
    else:
        print('\nNo one is going to be lucky\n')    
        print(joining_dict)

else:
    print('\nNo one is joining for the party')

