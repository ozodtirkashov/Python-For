n = int(input("1-son >> "))


for i in range(6):
    son = int(input(f"{i + 2} -son >  "))


    if son < n:
        n = son

print("eng kichik son ",n)


    

