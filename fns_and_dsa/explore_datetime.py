from datetime import datetime, timedelta


def display_current_datetime():
  current_date = datetime.now()
  formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

  print("--- Part 1: Current Date and Time ---")
  print(f"Current date and time: {formatted_date}")

  return current_date


def calculate_future_date(current_date):
  print("\n--- Part 2: Calculate a Future Date ---")

  days_to_add_input = input("Enter the number of days to add to the current date: ")
  try:
    days_to_add = int(days_to_add_input.strip())
  except ValueError:
    print("Invalid number entered. Using 0 days.")
    days_to_add = 0

  time_difference = timedelta(days=days_to_add)
  future_date = current_date + time_difference
  formatted_future_date = future_date.strftime("%Y-%m-%d")

  print(f"Future date (after {days_to_add} days): {formatted_future_date}")


def main():
  current_datetime_object = display_current_datetime()
  calculate_future_date(current_datetime_object)


if __name__ == "__main__":
  main()