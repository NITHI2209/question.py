#question:
# *****
#  ****
#   ***
#    **
#     *
code:
n = int(input("enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
#sample:
# enter the number of rows: 8
# ********
#  *******
#   ******
#    *****
#     ****
#      ***
#       **
#        *
