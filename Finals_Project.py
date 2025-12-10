import os

os.system("clear")

print("\t<===========================================================>")
print("\n\t\t\t\tMENU SYSTEM")
print("\n\t<==========================================================>")


while True:
    choose = input("\n A. START\n B. WHAT IS PYTHON?\n C. EXIT SYSTEM\n\n CHOOSE FROM ABOVE: ").lower()

    if choose == 'a':
        os.system("clear")

        while True:

            learn = input("WHAT DO YOU WANT TO LEARN?\m\n A. PRINTING STATEMENT\n B. VARIABLES\n C. OPERATORS\n D. CONDITIONAL\n E. LOOPS\n F. LISTS\n G. FUNCTION\n H. EXIT\n\n CHOOSE FROM ABOVE: ").lower()


            if learn == 'a':

                while True:
                    cute = input("\n A. PRINT STATEMENT\n B. INPUT\n C. BACK\n\n CHOOSE FROM ABOVE: ")

                    if cute == 'a':
                        print("\n THIS IS THE EXAMPLE OF PRINTING: \n\n <========== print('HELLO WORLD')==========>")

                        print("\n OUTPUT:  HELLO WORLD")


                        while True:
                            cute = input("\n ==========================================\n\n A. EXPLAIN HOW PRINT WORKS\n B. Try to code it\n C. BACK\n\n ===========================================\n CHOOSE FROM ABOVE: ").lower()

                            if cute =='a':
                                print("\n THE PRINT() WORKS BY TELLING THE COMPUTER WHAT TO SHOW ON THE SCREEN")
                                print(" WHEN YOU TYPE print('cute') THE SCREEEN OR COMPUTER WILL SHOW 'cute' ")

                            if cute == 'b':
                                print("\n TRY IT")
                                print("=================================")
                                code = input("ENTER HERE: ")
                                print("\n OUTPUT: ")

                                try:
                                    exec(code)
                                except Exception as e:
                                    print(f"ERROR:{e}.  PLEASE TRY AGAIN LIKE print('Hello World)")


                            if cute == 'c':
                                break

                    else:
                        print("Invalid choice TRY AGAIN.")




                    if cute == 'b':
                        print("\n THIS IS THE EXAMPLE OF INPUT: \n\n name = input(' Enter name: ')")
                        print("\n print('Hello,' + name)")
                        print("\n OUTPUT (if yout enter 'princess': Hello,princess)")

                        print("\n EXPLANATION: The input() funtion asks the user for input and return it as a sting")

                        while True:
                            cute = input("\n====================\n\n A. EXPLAIN THE INPUT SYSTEM\n B. Try it\n C. BACK")
                            print("\n CHOOOSE FROM ABOVE: ").lower()

                            if cute == 'a':
                                print("===========================================================")
                                print("Input is the information, data, or commands that a user or system provides to a computer or program so it can process that information and produce an output.")
                                print("===========================================================")


                            if cute == 'b':
                                print("\n TRY IT")
                                code = input("ENTER HERE: ")

                                try:
                                    exec(code,{})
                                except Exception as e:
                                    print("ERROR IN YOUR CODE: {e} PLEASE TRY AGAIN LIKE print name = input('ANY NAME:); print(name) ")

                            
                            if cute == 'c':
                                break

                    else:
                        print("INVALID CHOICE. TRY AGAIN")


            if learn == 'b':
                
                while True:

                    
                    print("\n===== MAIN MENU: VARIABLES =====")
                    print("1. What Are Variables?")
                    print("2. Types of Variables")
                    print("3. Try it")
                    print("4. Exit")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        print("\n--- What Are Variables? ---")
                        print("Variables store data in a program.")

                    elif choice == "2":
                        while True:
                            print("\n=== SUB-MENU: TYPES OF VARIABLES ===")
                            print("1. Integer")
                            print("2. Float")
                            print("3. String")
                            print("4. Back")

                            sub = input("Enter your choice: ")

                            if sub == "1":
                                print("Integer = whole numbers (e.g., 1, 20, -5)")
                            elif sub == "2":
                                print("Float = numbers with decimals (e.g., 3.14, 1.5)")
                            elif sub == "3":
                                print("String = text (e.g., 'hello')")
                            elif sub == "4":
                                break
                            else:
                                print("Invalid choice!")


                    elif choice == '3':
                        print("\n TRY IT")
                        code = input("ENTER HERE: ")

                        try:
                            exec(code,{})
                        except Exception as e:
                             print("ERROR IN YOUR CODE: {e}. TRY AGAIN ")
                        

                    elif choice == "4":
                        print("Goodbye!")
                        break

                    else:
                        print("Invalid choice!")

                        continue




                    


                    




                                
        



                    



                                
                            


            




            



    
