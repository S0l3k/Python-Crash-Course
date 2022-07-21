current_users = ['alton john', 'tim', 'machoman', 'baby', 'catdog']
new_users = ['tim', 'elezabat', 'kiss_my_ass', 'catdog', 'PL']
save_current_users = current_users[:]

#for i in range(len(save_new_users)):
 #   save_new_users[i] = save_new_users[i].lower()
#print(save_new_users)
#for i in range(len(save_current_users)):
 #   save_current_users[i] = save_current_users[i].lower()
#print(save_current_users)

#for save_current_users in save_current_users:
#    save_current_users = save_current_users.lower()
    #print(save_current_users)
#for save_new_users in save_new_users:
#    save_new_users = save_new_users.lower()
   #print(save_new_users)

for new_users in new_users:
    if new_users in current_users:
        print('You have not use this username,', new_users,', rename please!')
    else:
        print('This name ,',new_users, ', available!')