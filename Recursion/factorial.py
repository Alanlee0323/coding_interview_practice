def findFactorialRecursive(number): #5
    if number == 2:
        return 2
    return number * findFactorialRecursive(number - 1)
    
def findFactorial(number):
    answer = 1
    for i in range(2, number+1):
        answer = answer * i
    return answer 
print(findFactorial(7))