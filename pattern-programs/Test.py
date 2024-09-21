n = int(input("Provide an integer input: "))
# n = 4

for i in range(n):
    for j in range(n-i):
        print(' '* (n-i) + '* '* (j+1))
    print()
print()


#    *
#   * *
# *  *  *