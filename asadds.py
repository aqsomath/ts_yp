from datetime import datetime

# Define two datetime objects
start_time = datetime.now()
end_time = datetime(2024, 4, 7, 23, 0, 0)

# Subtracting datetime objects
time_difference = end_time - start_time

# Convert timedelta to seconds
time_difference_seconds = time_difference.total_seconds()

print("Time difference in seconds:", time_difference_seconds)
