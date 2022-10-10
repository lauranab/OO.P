
while sentinel != "stop":
score = float(input("Enter Score: "))
if score >= 0.9 :
    print("You scored grade A.")
    elif score >= 0.8 :
        print("You scored grade B.")
        elif score >= 0.7 :
            print("You scored grade C")
            elif score >= 0.6:
                print("You scored grade D")
                elif score < 0.6 :
                    print("You scored grade F")
                    else:
                        print("PLEASE ENTER THE CORRECT GRADE") 

                        sentinel = input("Enter stop if you wis to exit the program")
                        
                    



