my_list = ['physics', 'chemistry', 'biology', 'math', 'english']
newlist = my_list[:] # makes a copy of the list

for item in my_list:
    print('Not Done')
    item = item.upper()
    item = 'Subject: ' + item
    print(item)

print('Done')