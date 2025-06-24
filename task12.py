n = int(input("N ni kiriting: "))

juft_yigindi = 0
toq_yigindi = 0

for i in range(1, n +1):
    if i % 2 == 0:

        juft_yigindi += i
    else:
        toq_yigindi += i
print(juft_yigindi, ",", toq_yigindi)        