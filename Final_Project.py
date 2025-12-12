import os

os.system("clear")

print("\t🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
print("\n\t\t\t\t\t🗂️ 📁 MENU SYSTEM 🛠️ ⚙️")
print("\n\t🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")


while True:
    choose = input("\n A. START\n B. WHAT IS PYTHON?\n C. EXIT SYSTEM\n\n CHOOSE FROM ABOVE: ").lower()

    if choose == 'a':
        os.system("cls")

        while True:

            learn = input("\n\n WHAT DO YOU WANT TO LEARN?\n\n 1. PRINTING STATEMENT\n 2. VARIABLES\n 3. OPERATORS\n 4. CONDITIONAL\n 5. LOOPS\n 6. LISTS\n 7. FUNCTION\n 8. EXIT\n\n CHOOSE FROM ABOVE: ").lower()


            if learn == '1':
                os.system('cls')

                while True:
                    print("\n🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️")
                    print("\n\t PRINT STATEMENT")
                    print("\n🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️")
                    print("\n1. Print")
                    print("2. Input")
                    print("3. Try to code it")
                    print("4. BACK")

                    Hirap = input("Enter your choice: ")

                    if Hirap == '1':
                        os.system('cls')
                        while True:

                            print("\t 🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤 PRINTING 🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤")
                            print("\n\n EXAMPLE OF PRINTING: \n\n print(\"HELLO WORLD\")")
                            print("\n1. Explain how printing work")
                            print("2. BACK")

                            Hirap = input("Enter your choice: ")

                            if Hirap == '1':
                                print("\n HE PRINT() WORKS BY TELLING THE COMPUTER WHAT TO SHOW ON THE SCREEN. WHEN YOU TYPE print(\"cute\") THE SCREEEN OR COMPUTER WILL SHOW cute ")

                            if Hirap == '2':
                                print("GOING BACK...")
                                break
                            else:
                                print("INVALID CHOICE. TRY AGAIN")
                                continue


                    elif Hirap == '2':
                        os.system('cls')
                        while True:
                            print("\n\n\t🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤 INPUT 🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤")
                            print("\n\n The input() function in programming (like Python) is used to take information from the user.")
                            print("\n\n EXAMPLE:\n name = input('Enter name:')") 
                            print("\n print('Hello,' + name)")
                            print("\n OUTPUT (if yout enter 'princess': Hello, princess)")
                            print("\n1. Explain how input work")
                            print("2. Back")

                            Hirap = input ("\nEnter your choice: ")

                            if Hirap == '1':
                                print("input() works by asking the user to type something on the keyboard, then it takes what the user types and stores it in a variable so the program can use it later")

                            elif Hirap == '2':
                                print("GOING BACK...")
                                break
                            else:
                                print("INVALID CHOICE")

                    elif Hirap == '3':
                        print("\n TRY IT")
                        code = input("ENTER HERE: ")

                        try:
                            exec(code,{})
                        except Exception as e:
                             print("ERROR IN YOUR CODE: {e}. TRY AGAIN ")
                        

                    elif Hirap == "4":
                        print("GOING BACK...")
                        break

                    else:
                        print("Invalid choice!")

                        continue
                                            
                            


            elif learn == '2':
                os.system('cls')
                
                while True:

                    
                    print("\n🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹")
                    print("\n\t\t VARIABLES")
                    print("\n🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹")
                    print("\n1. What Are Variables?")
                    print("2. Types of Variables")
                    print("3. Try it")
                    print("4. Exit")

                    choice = input("\n\nEnter your choice: ")

                    if choice == "1":
                        print("\n==== What Are Variables? ====")
                        print("A variable is like saving a contact in your phone. Instead of typing the whole number everytime, you just use the saved name like 'The name = variables")
                                    
                    elif choice == "2":
                        while True:
                            print("\n======== TYPES OF VARIABLES ========")
                            print("1. Integer")
                            print("2. Float")
                            print("3. String")
                            print("4. Back")

                            other = input("\n\nEnter your choice: ")

                            if other == "1":
                                print("Integer = A variable that stores whole numbers (no decimal point)")
                                print("For Example: \n age = 20\n student = 54\n year = 2025")
                            elif other == "2":
                                print("Float = A variable that stores numbers with decimals ")
                                print("For Example: \n Temperature = 36.5\n Grade = 90.75\n Payment = 250.00")
                            elif other == "3":
                                print("String = A variable that store text, like word, letters, and name")
                                print("String = For Example\n name ='rie'\n section = 'BSIT-1B'\n message = 'How are you, bebe?")
                            elif other == "4":
                                print("GOING BACK...")
                                break
                            else:
                                print("Invalid choice!")
                                continue


                    elif choice == '3':
                        print("\n TRY IT")
                        code = input("ENTER HERE: ")

                        try:
                            exec(code,{})
                        except Exception as e:
                             print("ERROR IN YOUR CODE: {e}. TRY AGAIN ")
                        

                    elif choice == "4":
                        print("GOING BACK")
                        break

                    else:
                        print("Invalid choice!")

                        continue
            
            elif learn == '3':
                os.system('cls')

                while True:

                    print("\n 🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷")
                    print("\n\t\t OPERATORS")
                    print("\n 🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷🌷")
                    print("\n1. What are Operators")
                    print("2. Types of Operators")
                    print("3. Try to code it")
                    print("4. Exit")

                    choice = input("\n\nEnter your choice:")

                    if choice == '1':
                        print("\n>>>>>>> WHAT ARE OPERATORS <<<<<<<")
                        print("\n An operator is a symbol that tells the computer to do a specific operation, like adding numbers, comparing values, or checking conditions")
                    

                    elif choice == '2':
                        while True:
                            print("\n >>>>>>>> TYEPES OF OPERATORS <<<<<<<<")
                            print("\n1. Arithmetic operators")
                            print("2. Relational operators")
                            print("3. Logical operators")
                            print("4. Assignment operators")
                            print("5. EXIT")


                            Hirap = input("\n\n ENTER YOUR CHOICE:")

                            if Hirap == '1':

                                print("\n\n\t Arithmetic operator is used for math calculations")
                                print("\n EXAMPLE:\n + (additon)\n - (subtraction)\n * (multiplation)\n / (division)\n  % (modulus)")
                                print("\n like this\n 5 + 3 = 8\n 10 % 3 = 1")

                            elif Hirap == '2':

                                print("\n\n\t Rational operator is used to compare values and the results will be TRUE or FALSE.")
                                print("\n EXAMPLE:\n == (equal to)\n != (not equal to)\n > (greater than)\n < (less than)")
                                print("\n like this:\n 5 > 4 --> TRUE\n 7 == 10 --> FALSE")

                            elif Hirap == '3':

                                print("\n\n\t Logical operator is used for conditions and combining comparisons")
                                print("\n EXAMPLE:\n && (and)\n  || (or)\n ! (not)")
                                print("\n like this:\n (age > 18) && (age < 30)")

                            elif Hirap == '4':

                                print("\n\n\t Assignment operators is used to store values in variables")
                                print("\n EXAMPLE: = (assign)\n += (add then assign)\n -= (subtract then assign)")
                                print("\n like this:\n x = 7\n x += 2 \n so the x becomes 9")

                            elif Hirap == '5':
                                print("GOING BACK...")
                                break
                            else:
                                ("\n INVALID CHOICE")
                                continue

                    elif choice == '3':

                        print("\n TRY IT")
                        code = input("ENTER HERE: ")


                        try:
                            exec(code,{})
                        except Exception as e:
                            print(f"ERROR IN YOUR CODE:{e}. PLSS TRY AGAIN")


                    elif choice == "4":
                        print("Goodbye! Have a good day")
                        break

                    else:
                        print("Invalid choice!")

                        continue


            elif learn == '4':
                os.system('cls')
                while True:

                    print("\n 🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼")
                    print("\n\t\t CONDTIONAL")
                    print("\n 🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼")
                    print("\n1. What are Conditional")
                    print("2. Types of Conditional")
                    print("3. TRY TO CODE IT")
                    print("4. EXIT")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        print("\n >>>>>>>> WHAT ARE CONDITION <<<<<<<<")
                        print("\n Condition are the statement that can check if something is True or False")
                        print("\n\n This is the basic keyword\n if - check a conditional\n elif - extra condition if the first is not true\n else - run when all condition above are false")

                    elif choice == '2':
                        while True:
                                print("==================================")
                                print("\n TYPES OF CONDITIONS")
                                print("\n==================================")
                                print("\n1.IF Statement")
                                print("2. IF - ELSE Statement")
                                print("3. IF - ELIF - ELSE Statement")
                                print("4. NESTED IF")
                                print("5. EXIT")

                                choice == input("Enter your choice: ")

                                if choice == '1':
                                    print(">>>>>>>>>> EXAMPLE OF IF STATEMENT <<<<<<<<<<")
                                    print("\n IF Statement used when you want to check one condition")
                                    print("\n EXAMPLE:\n if age >= 18:\n\tprint('adult')")
                                    continue
                                
                                elif choice == '2':
                                    print(">>>>>>>>>> EXAMPLE OF IF - ELSE STATEMENT <<<<<<<<<<")
                                    print("\n IF - ELSE Statement used when you want two options")
                                    print("\n EXAMPLE:\nif age >= 18:\n\tprint('adult')\nelse:\n\tprint('minor')")
                                    continue

                                elif choice == '3':
                                    print(">>>>>>>>>> EXAMPLE OF IF - ELIF - ELSE STATEMENT <<<<<<<<<<")
                                    print("\n IF - ELIF - ELSE used when you want to check many conditions")
                                    print("\n EXAMPLE:\nif grade >= 90:\n\tprint('Excellent)\nelif grade >= 75:\n\tprint('passed')\nelse:\n\tprint('failed')")
                                    continue

                                elif choice == '4':
                                    print(">>>>>>>>>> EXAMPLE OF  NESTED IF STATEMENT <<<<<<<<<<")
                                    print("\n NESTED IF an if inside another if")
                                    print("\n EXAMPLE:\nif age >= 18:\n\tif has_id:\n\t\tprint('You may enter')")
                                    continue

                                elif choice == '5':
                                    print("GOING BACK...")
                                    break
                                else:
                                    print("INVALID CHOICE")
                                    continue


                    elif choice == '3':
                        print("\n TRY IT")
                        code = input("ENTER HERE: ")


                        try:
                            exec(code,{})
                        except Exception as e:
                            print(f"ERROR IN YOUR CODE:{e}. PLSS TRY AGAIN")

                    elif choice == '4':
                        print("GOING BACK...")
                        break
                    else:
                        print("INVALID CHOICE!")
                        continue


            elif learn == "5":
                os.system('cls')
                while True:

                    print("\n 🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱")
                    print("\n\t\t LOOPS")
                    print("\n 🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱")
                    print("\n1. What are Loops?")
                    print("2. Types of Loops")
                    print("3. Try to code it")
                    print("4. EXIT")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        print(">>>>>>>> LOOPS <<<<<<<<<")
                        print("\n Loops let your code repeat something many times without writing it again")

                    elif choice == '2':
                        while True:
                            print("===================================")
                            print("\n TYPES OF LOOPS")
                            print("===================================")
                            print("\n1. for loop")
                            print("2. while loop")
                            print("3. EXIT")

                            choice = input("Enter your choice: ")


                            if choice == '1':
                                print(">>>>>>>>>> EXAMPLE OF FOR LOOP <<<<<<<<<<")
                                print("\n for loop used when you know how many times you want to repeat")
                                print("\n\n EXAMPLE: \nfor i in range(5):\n\tprint('Hello')")
                                print("\n THIS PRINTS \"Hello\" 5 times")

                            elif choice == '2':
                                print(">>>>>>>>>> EXAMPLE OF WHILE LOOP <<<<<<<<<<")
                                print("\n while loop used when you want to repeat as long as a condtion is true")
                                print("\n\n EXAMPLE: \nx = 1\nwhile x <= 5:\n\tprint(x)\n\tx += 1")
                                print("\n THIS PRINT 1 TO 5")


                            elif choice == '3':
                                print("GOING BACK...")
                                break
                            else:
                                print("INVALID CHOICE")
                                continue

                    elif choice == '3':

                        print("\n TRY IT")
                        code = input("ENTER HERE: ")


                        try:
                            exec(code,{})
                        except Exception as e:
                            print(f"ERROR IN YOUR CODE:{e}. PLSS TRY AGAIN")


                    elif choice == '4':
                        print("GOING BACK...")
                        break
                    else:
                        print("INVALID CHOICE!")
                        continue


            elif learn == '6':
                os.system('cls')

                while True:
                    
                    print("\n 🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻")
                    print("\n\t\t LISTS")
                    print("\n 🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻")
                    print("\n1. What are list?")
                    print("2. Types of lists")
                    print("3. Try to code it")
                    print("4. EXIT")

                    choice = input("Enter your choice here: ")

                    if choice == '1':
                        print(">>>>>>>>>> LISTS <<<<<<<<<<")
                        print("\n A list is a container that can store many values in one variable")
                        print("\n\n EXAMPLE:\n fruits = [\"watermelon\", \"grapes\", \"orange\"]")

                    elif choice == '2':
                        while True:

                            print(">>>>>>>>>> TYPE OF LISTS <<<<<<<<<<")
                            print("\n1. Key things about lists")
                            print("2. Changing an item")
                            print("3. Adding items")
                            print("4. Removing item")
                            print("5. Lenght of list")
                            print("6. Looping through a list")
                            print("7. EXIT")


                            Hirap = input(" Enter your choice: ")

                            if Hirap == '1':
                                print(">>>>>>>>>> KEY THINGS ABOUT LIST <<<<<<<<<< ")
                                print("\n\n You can store many items\n EXAMPLE:\n numbers = [1,2,3,4,5]")
                                print("\n You can mix types\n EXAMPLE:\n mixed = [1,\"hello\", 3.5, True]")
                                print("\n You can also access item using index ( starting at 0)\n EXAMLE:\nfruit[0]\t # watermerlon\nfruit[1]\t # grapes")
                                
                            elif Hirap == '2':
                                print(">>>>>>>>>> EXAMPLE OF CHANGING AN ITEM <<<<<<<<<< ")
                                print("\n\n The lists are editable\n EXAMPLE:\n fruits [1] = \"banana\"")

                            elif Hirap == '3':
                                print(">>>>>>>>>> EXAMPLE OF ADDING ITEMS <<<<<<<<<< ")
                                print("\n\n You can add items\n EXAMPLE:\n fruits.append(\"mango\")")

                            elif Hirap == '4':
                                print(">>>>>>>>>> EXAMPLE OF REMOVING ITEM <<<<<<<<<< ")
                                print("\n You can also remove item\n EXAMPLE:\n fruits.remove(\"grapes\")")
                                print("or\n fruits.pop(0)\t # removes item at index 0")

                            elif Hirap == '5':
                                print(">>>>>>>>>> EXAMPLE OF LENGHT OF LISTS <<<<<<<<<< ")
                                print("\n\n EXAMPLE:\n len(fruits)")

                            elif Hirap == '6':
                                print(">>>>>>>>>> EXAMPLE OF LOOPING TROUGH A LIST <<<<<<<<<< ")
                                print("\n\n EXAMPLE:\nfor item in fruits:\n\tprint(item)")

                            elif Hirap == '7':
                                print("GOING BACK...")
                                break
                            else:
                                print("INVALID CHOICE")
                                continue
                
                    elif choice == '3':
                        print("\n TRY IT")
                        code = input("ENTER HERE: ")


                        try:
                            exec(code,{})
                        except Exception as e:
                            print(f"ERROR IN YOUR CODE:{e}. PLSS TRY AGAIN")


                    elif choice == '4':
                        print("GOING BACK...")
                        break
                    else:
                        print("INVALID CHOICE!")
                        continue

                        

            elif learn == '7':
                os.system('cls')

                while True:
                    print("\n 🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿")
                    print("\n\t\t   FUNCTIONS")
                    print("\n 🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿")
                    print("\n1. What are Functions")
                    print("2. Types of function")
                    print("3. Try to code it")
                    print("4. Exit")

                    Hirap = input("Enter your choice: ")

                    if Hirap == '1':
                        print(">>>>>>>>>> FUNCTIONS <<<<<<<<<< ")
                        print("\n\n A funtion is a block of code that does something and you can use it again")
                        
                    elif Hirap == '2':
                        while True:

                            print(">>>>>>>>>> TYPES OF FUNCTIONS <<<<<<<<<< ")
                            print("\n1. Built in")
                            print("2. User defined")
                            print("3. EXIT")


                            Hirap = input("Enter your choice: ")

                            if Hirap == '1':
                                print(">>>>>>>>>> EXAMPLE OF BUILT IN FUNCTION <<<<<<<<<< ")
                                print("\n Built in is a function that are already provided by the programming language. You can use them anytime without creating them")
                                print("\n\n EXAMPLE:\n print(\"Hello, love!\")")
                                print("name = \"princess\"\nprint(len(name))\t # outputs 4")
                                print("x = 10\nprint(type(x))\t # shows the data type of x")

                            elif Hirap == '2':
                                print(">>>>>>>>>> EXAMPLE OF USER DEFINED FUNCTION <<<<<<<<<< ")
                                print("\n User defined are functions that you create yourself")
                                print("\n\n EXAMPLE 1: SIMPLE GREETING\ndef greet():\n\tprint(\"Hi, bebe!\")")
                                print("\n EXAMPLE 2: FUNTION WITH PARAMETERS\ndef add(a,b):\n\treturn(a + b) ")
                                print("\n EXAMPLE 3: USER - DEFINED FUNCTION WITH NO PARAMETERS\ndef showMessage():\n\tprint(\"WELCOME TO THE EARTH\")")

                            elif Hirap == '3':
                                print("GOING BACK...")
                                break
                            else:
                                print("INVALID CHOICE")
                                continue

                    elif Hirap == '3':
                        print("\n TRY IT")
                        code = input("ENTER HERE: ")


                        try:
                            exec(code,{})
                        except Exception as e:
                            print(f"ERROR IN YOUR CODE:{e}. PLSS TRY AGAIN")


                    elif choice == '4':
                        print("GOING BACK...")
                        break
                    else:
                        print("INVALID CHOICE!")
                        continue

            elif learn == '8':
                print("QUITING THE SYSTEM. THANKYOU FOR RUNNING MY CODE:))")
                break
            else:
                print("INVALID CHOICE")

    elif choose == 'b':
        os.system('cls')
        print("\t💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚")
        print("\n\t\t\tPYTHON🐍🐍🐍")
        print("\n\t💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚💚")

        print("""\n\n Python is a high-level, easy-to-read, and beginner-friendly programming language used for creating a wide range of applications. It was developed by Guido van Rossum and released in 1991 with the goal of making code simple, clear, and powerful. Python is widely used because its syntax looks almost like English, making it easier for students and professionals to learn. It supports many programming styles, including object-oriented and procedural programming, and it comes with thousands of libraries that help in web development, data science, artificial intelligence, automation, gaming, and more. Python is also known for being flexible, portable, and open-source, which means anyone can use and modify it for free. Because of its simplicity and power, Python has become one of the most popular and most important programming languages in the world today, love. 🤍💖🖥️ ⌨️ 🖱️
 """)
        
    elif choose == 'c':
        
        print("GOODBYEEE, dapat ni try mo")
        break
    else:
        print("INVALID CHOICE! TRY AGAIN")



                #Sobrang sakit kamay ko sir tapos sobrang lamig nunh aircon sa cl3. Parang hotdog na po kami sa ref dito
                #Ang wish lang po namin ay medyo hinaan anf aircon hehehe charot lang po
                #Sir sulit ang pagod maalam na ako ngayon mag code, sir. Parang hindi na ako mag shift sa enterep neto




                            
                                



                            







                    
                                

                            








                    




                            





























                        


                            


                        


                    


                    




                                
        



                    



                                
                            


            




            


