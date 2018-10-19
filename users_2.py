current_users=['admin','root','jack','peter','wuhang']
new_users=['admin','root','wangjun','jeck','peck']
for new_user in new_users:
    if new_user in current_users:
        print(new_user+" used,""Need to input other users")
    elif new_user not in current_users:
        print(new_user+","+" User name not used")
