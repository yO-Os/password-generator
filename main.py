#pull request

import random
password = []

num = input("number of characters")

for x in range(0,int(num)):
    randomnum = int(random.random()*126)+65
    password.append(chr(randomnum))
for n in password:
    print(n)

    
