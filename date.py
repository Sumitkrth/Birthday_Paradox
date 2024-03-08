
import random
from datetime import datetime
from calendar import monthrange

# Function to get the number of days in a given month
def days_in_month(year, month):
    _, last_day = monthrange(year, month)
    return last_day

# Function to generate a random date with only day and month
def random_date_day_month():
    random_month = random.randint(1, 12)
    random_day = random.randint(1, days_in_month(2022, random_month))
    return datetime(2022, random_month, random_day)

# Generate and print 30 random dates with only day and month
random_dates = [random_date_day_month().strftime("%d-%m") for _ in range(30)]
random_dates.sort()
print(random_dates)


