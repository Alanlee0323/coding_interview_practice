def fibonacciRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        para1 = n-2
        para2 = n-1
        return fibonacciRecursive(para1)+ fibonacciRecursive(para2)

ans = {0:0, 1:1}
def fibonacciMemo(n):
    global ans
    
    if n in ans:
        return ans[n]
    
    result = fibonacciMemo(n - 1) + fibonacciMemo(n - 2)
    ans[n] = result

    return result

print(fibonacciMemo(7))