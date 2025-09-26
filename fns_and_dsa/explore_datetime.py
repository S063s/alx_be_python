def display_current_datetime():
    from datetime import datetime
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Enter a number of days: {formatted_datetime}")

def calculate_future_date():
    from datetime import datetime, timedelta
    future_days = int(input("Enter the number of days to add to the current date: ").strip())
    current_date = datetime.now()
    future_date = current_date + timedelta(days=future_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date after {future_days} days will be: {formatted_future_date}")