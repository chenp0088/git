users=['admin','root','peter','psla','seare']
for user in users:
    print("Hello "+user+'.')
    if user=='admin':
        print("Hello "+user+','"would you like to see a status report?")
    else:
        print("Hello Eric,thank you for logging in again")
