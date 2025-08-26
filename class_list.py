# Write a program that asks for the names of 
# all of the classes you are taking this semester
# Save these class names in a list.
# Print all the items in the list, one per line.

class_names_list = []  # empty list 

while True:
    class_name = input('Enter the name of a class you are taking or enter to stop : ')
    # if class_name == '':  
    # if len(class_name) == 0:
    if not class_name:      # pythonic truthiness and falsiness 
        # things that are false are 0, empty string, empty list, False 
        break  # end loop 
    class_names_list.append(class_name)
    print(class_names_list)


for item in class_names_list:
    print(item)