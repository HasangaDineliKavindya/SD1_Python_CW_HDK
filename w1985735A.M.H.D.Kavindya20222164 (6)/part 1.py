# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
#Westminster ID:w19857350  # Name : A.M.H.D.Kavindya # IIT Number :20222164
total=0
count_of_progress=0
count_of_trailer=0
count_of_retriever=0
count_of_exclude=0
option=int(input("Enter option '1' for  version for students or option '2' for staff version: "))

if option==1: 
    print("version for students ")
    print()
    
    while True:
        while True:
            try:
               Pass=int(input("Please enter your credits at pass: "))
               if Pass not in range(0,121,20):
                   print("Out of range.") #check whether pass is in  range or not
                   print()
                   continue
               else:
                   break
            except ValueError:
                print("Integer required") #Integer required 
                print()
                
        while True:
            try:
                defer=int(input("Please enter your credit at defer: "))
                if defer not in range(0,121,20):
                   print("Out of range.") #check whether defer is in range or not
                   print()
                   continue
                else:
                    break
            except ValueError:
                print("Integer required")#integer required part
                print()
                
        while True:
            try:
               fail=int(input("Please enter your credit at fail: "))
               if fail not in range(0,121,20):
                   print("Out of range.") #check whether fail is in range or not
                   print()
                   continue
               else:
                   break
            except ValueError:
                print("Integer required")#integer required part
                print()
                
        if (Pass+defer+fail) != 120: #check whether count is equal to 120 or not
          print("Total incorrect.") 
          print()
          continue

        if (Pass in range(0,121,20)) and (defer in range(0,121,20)) and (fail in range(0,121,20)):
          if Pass==120:
            print("Progress")
            print()
            break
          elif Pass==100:
            print("Progress (module trailer)")
            print()
            break
          elif (Pass==80) or (Pass==60) or (Pass==40 and defer>=20) or (Pass==20 and defer>=40) or (Pass==0 and defer>=60):
            print("Module retriever")
            print()
            break
          else:
            print("Exclude")
            print()
            break
          break
        break
        

elif option == 2:
  
    
    

    print("Staff Version ")
    print()

    progress_list=[]
    trailer_list=[]
    retriever_list=[]
    exclude_list=[]

    while True:
        valid_inputs1=[]
        valid_inputs2=[]
            
        try:
            Pass=int(input("Enter your total PASS credits: "))
            if Pass not in range(0,121,20):
                print("Out of range.")
                print()
                continue
            else:
                valid_inputs1.append(Pass)
                
            defer=int(input("Enter your total DEFER credits: "))
            if defer not in range(0,121,20):
                print("Out of range.")
                print()
                continue
            else:
                valid_inputs1.append(defer)

            fail=int(input("Enter your total FAIL credits: "))
            if fail not in range(0,121,20):
                print("Out of range.")
                print()
                continue
            else:
                valid_inputs1.append(fail)
                
            if (Pass+defer+fail) != 120:
               print("Total incorrect.")
               print()
               continue
            else:
                valid_inputs2 = valid_inputs1

            if (Pass in range(0,121,20)) and (defer in range(0,121,20)) and (fail in range(0,121,20)):
                if Pass==120:
                    print("Progress")
                    print()
                    count_of_progress += 1
                    progress_list.append(valid_inputs2)

                elif Pass==100:
                    print("Progress (module trailer)")
                    print()
                    count_of_trailer += 1
                    trailer_list.append(valid_inputs2)               

                elif (Pass==80) or (Pass==60) or (Pass==40 and defer>=20) or (Pass==20 and defer>=40) or (Pass==0 and defer>=60):
                    print("Module retriever")
                    print()
                    count_of_retriever += 1
                    retriever_list.append(valid_inputs2)                

                else:
                    print("Exclude")
                    print()
                    count_of_exclude += 1
                    exclude_list.append(valid_inputs2)
                    
        except ValueError:
            print("Integer required")
            print()
            continue

        print("Would you like to enter another set of data?")
        while True:
            forward=str(input("Enter 'y' for yes or 'q' to quit and view results: "))# option to continue or quit
            print()
            respond=forward.lower()
            if forward in ["y","q"]:
                break
            else:
                print("Wrong input!")
                print("You should enter 'y' or 'q'")
                continue

        if respond not in ("y","q"):
            print("Invalid input! ")
            
        if respond=="y":
            continue

        elif respond=="q":
            break
if option==2:
    # print the histogram
    print("Histogram")
    print("Progress", count_of_progress, ":", "*" * count_of_progress)
    print("Trailer", count_of_trailer, ":", "*" * count_of_trailer)
    print("Retriever", count_of_retriever, ":", "*" * count_of_retriever)
    print("Excluded", count_of_exclude, ":", "*" * count_of_exclude)
    print(count_of_progress + count_of_trailer + count_of_retriever + count_of_exclude, "outcomes in total.")


   
