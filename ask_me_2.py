name = input("Please Enter Your Name: ")

if name.isalpha(): #isalpha() function checks if user input contains only letters
    print("Hello " + name)
else:
    print("Hello Stranger")