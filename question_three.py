# i)
age=int(input("Enter your age:"))
if (age>=18):
    print("You are eligible")
else:
     print("You are not eligible")



# ii)
def grade_students():
       mark=int(input("Enter mark:"))
       if(mark>=90):
            print('A')
       elif (80<=mark<=89):
            print('B')
       elif (70<=mark<=79):
            print('C')
       elif (60<=mark<=69):
            print('D')
       elif(mark<60):
            print("F")
grade_students()
# iii)
# testing with 85
def grade_students(mark):
  
       if(mark>=90):
            print('A')
       elif (80<=mark<=89):
            print('B')
       elif (70<=mark<=79):
            print('C')
       elif (60<=mark<=69):
            print('D')
       elif(mark<60):
            print("F")
grade_students(85)


# v
def grade_students(mark):
     
       if(mark>=90):
            print('A','Excellent')
            
       elif (80<=mark<=89):
            print('B','Excellent')
          
       elif (70<=mark<=79):
            print('C','Good')
            
       elif (60<=mark<=69):
            print('D','Satisfactory')
        
       elif(mark<60):
            print("F",'Needs Improvement')
            
            
            # vi)
            
grade_students(78)

# iv)
def grade_students(mark):
    
       if(mark>=90):
            print('A')
       elif (80<=mark<=89):
            print('B')
       elif (70<=mark<=79):
            print('C')
       elif (60<=mark<=69):
            print('D')
       elif(mark<60):
            print("F")
    #    elif((type(mark))!==int):
    # #    elif(mark.isNumeric()):
            print('Invalid input')
grade_students("we")