def get_file_type(extension_type_str, file_list):
    extension_type_pairs = extension_type_str.split(';')
    extension_type_dict = {}
    
    for pair in extension_type_pairs:
        extension, file_type = pair.split(',')
        extension_type_dict[extension] = file_type
    
    file_type_dict = {}
    
    for filename in file_list:
        file_parts = filename.split('.')
        
        if len(file_parts) > 1:
            extension = file_parts[-1]
            file_type = extension_type_dict.get(extension, "unknown")
        else:
            file_type = "unknown"
        
        file_type_dict[filename] = file_type
    
    return file_type_dict

# Accept input from the user
extension_type_str = input("Enter extension and type values in the form of 'extension1,type1;extension2,type2': ")
file_list_str = input("Enter a list of filenames separated by spaces: ")
file_list = file_list_str.split()

# Call the get_file_type function and print the result
result = get_file_type(extension_type_str, file_list)
print(result)
