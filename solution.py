import math
iterator = 0
accumulator = 0.00000
while iterator <= 50:
    accumulator += float(math.factorial(50 + iterator)*pow(.5, 50)*pow(.5,iterator)*(50-iterator)/(math.factorial(iterator)*math.factorial(50)))
    iterator += 1
print("The expected value is " + str(accumulator))
