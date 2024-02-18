# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
#Westminster ID:w19857350  # Name : A.M.H.D.Kavindya # IIT Number :20222164
total=0
count_of_progress=0
count_of_trailer=0
count_of_retriever=0
count_of_exclude=0
option=int(input("Enter option '1' for  version for students or option '2' for staff version: "))

if option == 1:
    

    print("Student Version ")
elif option == 2:
    print("Staff Version ")
    student=open('studentscore.txt','w')
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
                student.write("Progress - ")
                

            elif Pass==100:
                print("Progress (module trailer)")
                print()
                count_of_trailer += 1
                trailer_list.append(valid_inputs2)
                student.write("Progress (module trailer) - ")
                

            elif (Pass==80) or (Pass==60) or (Pass==40 and defer>=20) or (Pass==20 and defer>=40) or (Pass==0 and defer>=60):
                print("Module retriever")
                print()
                count_of_retriever += 1
                retriever_list.append(valid_inputs2)
                student.write("Module retriever - ")
                
                

            else:
                print("Exclude")
                print()
                count_of_exclude += 1
                exclude_list.append(valid_inputs2)
                student.write("Exclude - ")
                
            student.write(str(Pass)+','+str(defer)+','+str(fail))    
            student.flush()
            student.write('\n')   
                
    except ValueError:
        print("Integer required")
        print()
        continue
    if option==1:
        import sys 
        sys.exit()

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
student.close()
# print the histogram
print("Histogram")
print("Progress", count_of_progress, ":", "*" * count_of_progress)
print("Trailer", count_of_trailer, ":", "*" * count_of_trailer)
print("Retriever", count_of_retriever, ":", "*" * count_of_retriever)
print("Excluded", count_of_exclude, ":", "*" * count_of_exclude)
print(count_of_progress + count_of_trailer + count_of_retriever + count_of_exclude, "outcomes in total.")

print("part 2")                     
for i in progress_list:
    print("Progress -",  str(i).strip("[]")) #print progress list
for i in trailer_list:
    print("Progress (module trailer) -",  str(i).strip("[]")) #print  Progress(module trailers) list
for i in retriever_list:
    print("Module retriever -", str(i).strip("[]")) #print  module retriever list
for i in exclude_list:
    print("Exclude –", str(i).strip("[]")) #print  exclude list

print("\nPart 3\n")
student=open('studentscore.txt','r')
scores=student.readlines()
for line in scores:
        
    if line.startswith("Progress - "):
                       print(line.strip('\n'))
student.seek(0)
for line in scores:
    if line.startswith("Progress (module trailer) - "):
                   print(line.strip('\n'))
student.seek(0)
for line in scores:
    if line.startswith("Module retriever - "):
                       print(line.strip('\n'))
student.seek(0)
for line in scores:
    if line.startswith("Exclude - "):
                   print(line.strip('\n'))
