#Perform intersection operation on list

def list_intersection(list1, list2):
    return list(set(list1) & set(list2))

list1= input("Enter the elements of the first list separated by spaces:").split()
list2=input("Enter the elements of the second list separated by spaces:").split()

#display the original lists
print("\nFirst List:",list1)
print("Second list:",list2)

#find the intersection of the two lists
intersection_result =list_intersection(list1,list2)

#display the intersection result
print("\nIntersection of the two lists:",intersection_result)