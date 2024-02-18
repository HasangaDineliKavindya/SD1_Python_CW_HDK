
forward = 0
Student_count = 1
Scores ={}

while True:
    while True:
        in_number = input("Enter your Index number: ")
        if len(in_number) != 8:
            print("Invalid Index.") #checking for 8 charachters
            print()
            continue
        if in_number[0] != "w":
            print("Invalid Index.")#check whether first charachter is w
            print()
            continue
       
        break
          
    while True:
        try:
            Pass=int(input("Enter your total PASS credits: "))
            if Pass not in range(0,121,20): 
                print("Out of Range.") #check whether Pass is in range or not
                print()
                continue
            else:
                break
        except ValueError:
            print("Integer required") #integer required part
            print()
    while True:
        try:
            defer=int(input("Enter your total DEFER credits:"))
            if defer not in range(0,121,20):
                print("Out of Range.") # check whether defer is in range or not
                print()
                continue
            else:
                break
        except ValueError:
            print("Integer required")#integer required part
            print()
    while True:
        try:
            fail=int(input("Enter your total FAIL credits:"))
            if fail not in range(0,121,20):
                print("Out of Range.") #check whether fail is in range or not
                print()
                continue
            else:
                break
        except ValueError:
            print("Integer required") #integer required part
            print()
            
    if (Pass + defer + fail) != 120: # check whether count is equal to 120 or not
        print("Total is incorrect.") 
        print()
        continue
    if (Pass in range(0,121,20)) and (defer in range(0,121,20)) and (fail in range(0,121,20)):
        if Pass==120 :
            print("Progress") 
            print()
            connect ="progress -",str([Pass,defer,fail]).strip('[]')
            Scores[in_number] = (' '.join(connect))
        elif Pass==100:
            print("Progress (module trailer)")
            print()
            connect ="Module trailer -",str([Pass,defer,fail]).strip('[]')
            Scores[in_number] = (' '.join(connect))
        elif (Pass == 80) or (Pass == 60) or (Pass == 40 and defer >=20) or (Pass == 20 and defer >= 40) or (Pass == 0 and defer >=60):
            print("Module retriever")
            print()
            connect ="Module retriever -",str([Pass,defer,fail]).strip('[]')
            Scores[in_number] = (' '.join(connect))
        else:
            print("Exclude")
            print()
            connect ="Exclude -",str([Pass,defer,fail]).strip('[]')
            Scores[in_number] = (' '.join(connect))
    print("Would you like to enter another set of data")
    while True : 
        forward=input("Enter 'y' for yes or 'q' to quit and view results: ") #option to continue or quit
        print()
        if forward=="y":
            Student_count+=1
            break
        else:
            if forward =="q":
                for i in Scores:
                    print(i,':',Scores[i])
                break
            else:
                print("Invalid  input please Enter y or q")
                continue
    if forward =="q":
        break
    else:
        continue         
