import random

# Initialize counters
rolls = 20  # Number of rolls (can be increased)
count_six = 0
count_one = 0
count_two_sixes_in_a_row = 0

# Simulate rolling the die
previous_roll = None
for _ in range(rolls):
    roll = random.randint(1, 6)
    
    # Count each occurrence of 6 and 1
    if roll == 6:
        count_six += 1
    if roll == 1:
        count_one += 1
    
    # Check for two 6s in a row
    if roll == 6 and previous_roll == 6:
        count_two_sixes_in_a_row += 1
    
    # Update previous roll
    previous_roll = roll

# Print statistics
print("Number of times 6 was rolled:", count_six)
print("Number of times 1 was rolled:", count_one)
print("Number of times two 6s were rolled in a row:", count_two_sixes_in_a_row)
