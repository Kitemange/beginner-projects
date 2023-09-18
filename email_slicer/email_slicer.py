#env!/usr/bin/env python3

#get email adress
with open("email_list.txt", "r") as file:
   email_list = file.readlines()#call on the file to read

#function to slice through the emails
#remove white spaces as well as split the text on finding the '@' character
def slice_mail(email):
    username, domain = email.strip().split('@')
    return username, domain

#processing of each email and storing the result
results = []
for email in email_list:
    username, domain = slice_mail(email)
    results.append((username, domain))

#print result
for username, domain in results:
    print("username: {}, Domain: {}".format(username, domain))