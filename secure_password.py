##  My way
import random
password = input("Enter the password ?\nSo i will tell you it is secure or not : ")
level = int(input("\n\tEnter the level of stongness : "))
newpass = [i for i in password]
random.shuffle(newpass)
panchutation  = [';','[','/','?','&','%','*','@','#','+','!','~','4','1','8']
random.shuffle(panchutation)
newpass.extend(panchutation[0:level])
random.shuffle(newpass)
print(f'\nHere is my suggestions : {"".join(newpass)}')
print(f'\nPassword you have Entered : {password}')
