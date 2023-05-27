def switch_dict_key_value(dictionary):
    return {value: key for key, value in dictionary.items()}

# Accept input from the user
import ast
input_dict_str = input("Enter a dictionary: ")
input_dict = ast.literal_eval(input_dict_str)

# Call the switch_dict_key_value function and print the result
switched_dict = switch_dict_key_value(input_dict)
print(switched_dict)
