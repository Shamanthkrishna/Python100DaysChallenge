# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cname = name1 + name2
name = cname.lower()

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
a = t+r+u+e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
b = l+o+v+e

score = int( str(a) + str(b) )

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")