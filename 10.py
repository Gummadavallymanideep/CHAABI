from datetime import datetime, timedelta

def get_date_before(date, n):
    date_format = '%y-%m-%d'

    # Convert date string to datetime object
    date_obj = datetime.strptime(date, date_format)

    # Calculate the date n days before
    before_date = date_obj - timedelta(days=n)

    # Convert the datetime object back to string representation
    before_date_str = before_date.strftime(date_format)

    return before_date_str

# Prompt the user for input
date = input("Enter the date (yy-mm-dd): ")
n = int(input("Enter the number of days: "))

# Call the function and print the result
result = get_date_before(date, n)
print(result)
