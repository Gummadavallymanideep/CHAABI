def sort_list_of_dicts(list_of_dicts, key):
    sorted_list = sorted(list_of_dicts, key=lambda x: x[key])
    return sorted_list

# Accept input from the user
import ast
input_list_str = input("Enter a list of dictionaries: ")
input_list = ast.literal_eval(input_list_str)

key = input("Enter the key to sort by: ")

# Call the sort_list_of_dicts function and print the result
sorted_list = sort_list_of_dicts(input_list, key)
print(sorted_list)
