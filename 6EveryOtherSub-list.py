def get_sublist_with_every_second_element(lst, start_index, end_index):
    sublist = lst[start_index:end_index+1:2]
    return sublist

# Accept input from the user
import ast
input_list_str = input("Enter a list: ")
input_list = ast.literal_eval(input_list_str)

start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

# Call the get_sublist_with_every_second_element function and print the result
result = get_sublist_with_every_second_element(input_list, start_index, end_index)
print(result)
