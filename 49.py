primes = []

for i in range(1, 100):
    for j in range(2, i):
        if i % j == 0:
            break
        else:  # agar shomarandeyi peyda nashavad else ejra mishavad
            primes.append(i)

print(primes)
