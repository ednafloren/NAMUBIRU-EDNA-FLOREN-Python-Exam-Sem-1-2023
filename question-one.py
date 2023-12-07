# i)
# creating a function
def calculate_area(radius):
    # storing the area in the viarable area
    area=3.14*radius*radius
    print(area)
calculate_area(5)    

# ii)
# function to find sum
def sum_of_nums(n):

   sum = 0

# using while loop
   while(n> 0):
       sum += n
       n -= 1
   print("The sum is", sum)
sum_of_nums(4)




# iii)
numbers=[1,3,5,7,9]
# removing element ant index 2
numbers.pop(2)
numbers.append(10)
print(numbers)

# iv)

# function to print even numbers in a list
even_numbers=[2,4,6,8,10]
# creating new empty list
neweven_numbers=[]
for x in numbers:
        if x%2==0:
         neweven_numbers.append(x)
print(f'EvenNumbers={neweven_numbers}')
  

# v)
student_info={'name':'Alice','age':20,'grade':'A'}
# adding new key and value
student_info['city']='New York'
student_info['age']=25
print(student_info)
# adding a value in a  new dictionary python
# vi)
newdict={}
original_dict={'a':3,'b':8,'c':7}
if(original_dict.values==5):
    newdict.append(original_dict.values)
    print(newdict)


