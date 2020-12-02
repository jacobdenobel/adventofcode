from collections import namedtuple

Password = namedtuple("Password", ["min","max", "letter", "password"])


def datagen():
    with open("data/2.txt", "r") as f:
        for line in f:
            policy, password = line.strip().split(":")
            p_range, p_letter = policy.split()
            yield Password(*map(int, p_range.split("-")),
                    letter=p_letter.strip(), password=password.strip())

count = 0
count2 = 0
for password in datagen():
    if password.password.count(password.letter) in range(password.min, password.max + 1):
        count += 1
    
    a,b = password.password[password.min-1], password.password[password.max-1]
    
    if a == password.letter and b != password.letter:
        count2 += 1
    elif a != password.letter and b == password.letter:
        count2 +=1


print("Q1", count)
print("Q2", count2)
 

    
