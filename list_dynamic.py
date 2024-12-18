#Create dynamic list where you will ask user to enter 5 elements in it and perform insert new element and 
# delete an element operation on it

dynamic_list=[]

#taking 5 elements as input from the user
for i in range(5):
    element= input(f"enter element {i+1}:")
    dynamic_list.append(element)
    
print("\nInitial List:", dynamic_list) 

#Inserting a new element into the list
new_element= input("\nEnter a new element to insert:")
dynamic_list.append(new_element)
print("List after inserting a new element:",dynamic_list)

#Deleting an element from the list
element_to_delete =input("\nEnter an element to delete:")
if element_to_delete in dynamic_list:
    dynamic_list.remove(element_to_delete)
    print("List after deleting the element:",dynamic_list)
else:
    print(f"Element '{element_to_delete}' not found in the list,")    