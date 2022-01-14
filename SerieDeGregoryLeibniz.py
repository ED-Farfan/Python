pi = 0
for i in range(0, 1000000):
    if(i % 2 == 0):
        pi += 4/(2*i+1)
    else:
        pi -= 4/(2*i+1)
print(pi)
