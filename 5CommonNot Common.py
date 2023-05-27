def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    non_common_elements = list(set(list1) ^ set(list2))
    return common_elements, non_common_elements

# Accept input from the user
import ast
mainstream_str = input("Enter the Mainstream list: ")
mainstream = ast.literal_eval(mainstream_str)

must_watch_str = input("Enter the must_watch list: ")
must_watch = ast.literal_eval(must_watch_str)

# Call the compare_lists function and print the result
common, non_common = compare_lists(mainstream, must_watch)
print(common)
print(non_common)
