from statistics import median, mean, mode, pstdev

alder = [25, 42, 42, 17, 56, 33, 23, 45]
median = median(alder)
gjennomsnitt = mean(alder)
typetall = mode(alder)
standardavvik = pstdev(alder)

print("Median er", median)
print("Gjennomsnittet er",round(gjennomsnitt,2))
print("Typetallet er" , typetall)
print("Standardavviket er", round(standardavvik,4))