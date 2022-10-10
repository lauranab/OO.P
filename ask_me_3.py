name = str(input("Please Enter Your Name: "))

if name.isalpha(): #isalpha() function checks if user input contains only letters
    print("Hello " + name)
    print("GoodByeeee")
    quit()
else:
    print("Hello Friend!!!!")
    age = int(input("How Old Are You Please: "))
          if age < 18:
               print("You Are Below Age Of Working")

                      elif age > 18 and age < 25:
                            print("You may Look For a job")
                                    elif age >= 25 and age < 30:
                                  print("You should already be having a job")
                                       elif age > 30 and age < 60:
                                           print("You can start a family")
                                                  elif age < 90 and age >= 60:
                                                      print("You are suitable for retirement")
                                                         else:
                                                                 print("YOUR AGE",age)
                                                                      print("GOODBYE",name)
                                                                           print("you are an alien")
        


    