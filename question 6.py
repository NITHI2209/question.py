#question
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
#code
n = int(input("enter the number of rows: "))
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i):
        print("*",end=" ")
    print()
 #sample:
# enter the number of rows: 7
# * * * * * * * 
#  * * * * * * 
#   * * * * * 
#    * * * * 
#     * * * 
#      * * 
#       * 
