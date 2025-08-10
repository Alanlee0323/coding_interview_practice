counter = 0
def inception():
    global counter
    if counter > 3: # base case
        return 'done'
    
    print(f"current counter: {counter}")
    counter += 1
    return inception()

result = inception()
print(result)