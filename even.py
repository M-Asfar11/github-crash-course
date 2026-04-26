try:
    num = int(input("Enter the number:"))
    if(num % 2 == 0):
        print("Number is even")
    else: 
        print("Number is odd")
except ValueError:
    print("Please enter integer!!!")
