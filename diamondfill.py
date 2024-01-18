n = int(input("Enter the number of rows: "))  

for i in range(0, n):  
    k=0
    for j in range(0, n-i):  
        print("  ",end="")  
    
    while(k!=2*i+1) :
        # printing full Triangle pyramid using stars  
        print("* ",end="")  
        k+=1
    print(" ")
# print()
                    # Outer loop in reverse order  
for i in range(n-1, -1, -1):  
    # Inner loop will print the number of space.  
    k=0
    for j in range(n-i-1, 0,-1):  
        print("  ",end="")  
 
    # This inner loop will print the number o stars  
    while(k != 2* i+2):
        print("* ", end="")
        k+=1
    print(" ")  