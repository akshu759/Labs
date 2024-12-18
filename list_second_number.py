#WAP to find second smallest element in the list

# Function to find the second smallest element
def find_second_smallest(lst):
    unique_elements = list(set(lst))  # Remove duplicates
    if len(unique_elements) < 2:
        return "The list must have at least two unique elements."
    unique_elements.sort()  # Sort the unique elements
    return unique_elements[1]  # Return the second smallest element

# Input list from the user
print("Enter the elements of the list (space-separated):")
user_list = list(map(int, input().split()))  # Convert input to a list of integers

# Find the second smallest element
result = find_second_smallest(user_list)

# Display the result
print("Second smallest element:", result)