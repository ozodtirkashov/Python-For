n = int(input("1-narxni kiriting: "))
eng_past_narx = n
eng_baland_narx = n
for i in range(4):
    n = int(input(f"{i + 2} - narxni kiriting: "))
    
    if  n > eng_baland_narx:
        eng_baland_narx = n

    if n < eng_past_narx:
        eng_past_narx = n

print(eng_past_narx, eng_baland_narx)            


