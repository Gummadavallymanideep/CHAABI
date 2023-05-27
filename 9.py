from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    date_format = '%y-%m-%d'

    # Convert date strings to datetime objects
    from_date_obj = datetime.strptime(from_date, date_format)
    to_date_obj = datetime.strptime(to_date, date_format)

    # Calculate the difference in days
    delta = abs((to_date_obj - from_date_obj).days)

    # Check if the difference is less than the specified number of days
    if delta < difference:
        return True
    else:
        return False

# Prompt the user for input
from_date = input("Enter the from date (yy-mm-dd): ")
to_date = input("Enter the to date (yy-mm-dd): ")
difference = int(input("Enter the difference in days: "))

# Call the function and print the result
result = check_date_difference(from_date, to_date, difference)
print(result)
