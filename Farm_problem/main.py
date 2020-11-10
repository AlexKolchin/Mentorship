chickens_legs = 2
cows_legs = 4
pigs_legs = 4
def animals(chickens, cows, pigs):
    sum = chickens * chickens_legs + cows * cows_legs + pigs * pigs_legs
    return sum

chickens = int(input("Please enter the number of chickens: "))
cows = int(input("Please enter the number of cows: "))
pigs = int(input("Please enter the number of pigs: "))

print(f"All your animals have {animals(chickens, cows, pigs)} legs")