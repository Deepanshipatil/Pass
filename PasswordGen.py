import random
letters=['a' ,'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','(',')','*','+','-']
numbers=['1','2','3','4','5','6','7','8','9','0']
print("Welcome to the password genrator")
n_letters=int(input("Enter how many letters you want to enter?\n"))
n_symbols=int(input("Enter how many symbols you want to enter?\n"))
n_numbers=int(input("Enter how many numbers you want to enter?\n"))
Password_li=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    Password_li += char 
for i in range(1,n_symbols+1):
    char =random.choice(symbols)
    Password_li+=char 
for i in range(1,n_numbers+1):
    char =random.choice(numbers)
    Password_li+=char 
    print(Password_li)
    random.shuffle(Password_li)
    print(Password_li)
password=" "
for i in Password_li:
    password+=char
print(password)
