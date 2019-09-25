def enough(cap, on, wait):
    # Your code here
    if cap - on - wait >= 0:
        return 0 #"He can fit all {0} passengers ".format(wait)
    left = cap - on - wait
    if left <0:
        left *= -1       
    return left #"He can't fit {0} out of {1} waiting".format(left,wait)

print (enough(100,60,50))