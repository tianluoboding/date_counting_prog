from datetime import datetime, timedelta

def date_difference(start_date, end_date):
    # Parse the input dates
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Calculate the difference
    delta = end_date - start_date

    # Break the difference into components
    total_seconds = delta.total_seconds()
    total_minutes = total_seconds / 60
    total_hours = total_minutes / 60
    total_days = delta.days
    full_weeks = total_days // 7
    remaining_days = total_days % 7
    total_weeks = full_weeks + (1 if remaining_days > 0 else 0)
    total_months = total_days // 30  # Approximation, as months vary in length

    # Output results
    print(f"Difference between {start_date} and {end_date}:")
    print(f"Months: {total_months} (approx.)")
    print(f"Weeks: {total_weeks}")
    print(f"Days: {total_days}")
    print(f"Hours: {total_hours:.2f}")
    print(f"Minutes: {total_minutes:.2f}")
    print(f"Seconds: {total_seconds:.2f}")


# Input from user
start_date = input("Enter the start date (yyyy-mm-dd): ")
end_date = input("Enter the end date (yyyy-mm-dd): ")

# Call the function
date_difference(start_date, end_date)