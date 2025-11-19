import os
import json


print("STUDENT INFORMATION SYSTEM")
print("<==========================>")

student_record = {}

while True:
    print("SELECT FROM THE FOLLOWING OPTION")
    print("A- ADD STUDENT RECORD")
    print("B- PRINT ALL STUDENT RECORD")
    print("C- SEARCH STUDENT RECORD")
    print("D- DELEK STUDENT RECORD")
    print("E- EDIT STUDENT RECORD")
    print("F- EXPORT STUDENT RECORD")
    print("G- EXIT SYSTEM")

    choice = input("SELECT FROM THE OPTION ABOVE ---->").lower()

    if choice == 'a':
        os.system('cls')
        print("\nADDING STUDENT RECORD")

        id_no = input("Please input student ID number --->\t").upper()
        first_name = input("Please input Student First Name --->\t").upper()
        second_name = input("Please input Student Second Name --->\t").upper()
        age = eval(input("Please input  Student Age --->\t"))
        course = input("Please input Student Course --->\t").upper()
        section = input("Please input Student Section --->\t").upper()
        
        student_record[id_no] = [first_name,second_name,age,course,section]
    
        print("DATA SAVE SUCCESSFULLY!")


        continue
    elif choice == 'b':
        os.system('cls')
        print("PRINTING STUDENT RECORD")

        for i, j in student_record. items():
            print(f"CODE - {i}, INFORMATION - {j}")
        continue
    elif choice== 'c':
        os.system('cls')
        print("STUDENT RECORD")
        search_id = input("Input Student ID for search -->\t").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("<=======================>")
                print("n\RECORD FOUND for ID {search_id}")

                for i in student_record[search_id]:
                    print(f"---- {i}")
                print("<============================>")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'd':
        os.system('cls')
        print("STUDENT RECORD")
        search_id = input("Input Student ID for search -->\t").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("<=======================>")
                print("n\REOCRD FOUND for ID {search_id}")

                for i in student_record[search_id]:
                    print(f"---- {i}")
                print("<============================>")

                student_record.pop(search_id)
                print("\nRECORD DELETED")
            else:
                print("NO RECORD FOUND")
            break
        continue

    elif choice == 'e':
        os.system('cls')

        print("EDIT/ MODIFY STUDENT RECORD")

        search_id = input("Input Students ID for search -->").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("<=======================>")
                print("n\REOCRD FOUND for ID {search_id}")

                for i in student_record[search_id]:
                    print(f"---- {i}")
                print("<============================>")

                first_name = input("Please input Student First Name --->\t").upper()
                second_name = input("Please input Student Second Name --->\t").upper()
                age = eval(input("Please input  Student Age --->\t"))
                course = input("Please input Student Course --->\t").upper()
                section = input("Please input Student Section --->\t").upper()


                student_record[search_id][0] = first_name
                student_record[search_id][0] = second_name
                student_record[search_id][0] = age
                student_record[search_id][0] = course
                student_record[search_id][0] = section

                print("DATA UPDATED")
            else:
                print("NO RECORD FOUND")

            break 
        continue
    elif choice== 'f':
        print("EXPORT STUDENT DATA")

        with open('student_record.json', 'w') as new_file:
            json.dump(student_record,new_file,indent=4)

        print("\n\nDATA EXPORTED TO JSON")
        continue
    
    
    elif choice == 'g':
        
        break
    
