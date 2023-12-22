import random
import matplotlib.pyplot as plt
from csv import writer

iterations = 10000000
scores = []

for i in range(iterations):
    rw_correct = 0
    math_correct = 0

    # Simulate answering questions for Reading & Writing modules and Math modules
    for question in range(27):  # Reading & writing module 1
        if random.randint(1, 4) == random.randint(1, 4):
            rw_correct += 1

    for question in range(27):  # Reading & writing module 2
        if random.randint(1, 4) == random.randint(1, 4):
            rw_correct += 1

    for question in range(22):  # Math module 1
        if random.randint(1, 4) == random.randint(1, 4):
            math_correct += 1

    for question in range(22):  # Math module 2
        if random.randint(1, 4) == random.randint(1, 4):
            math_correct += 1

    # Calculate scores
    rw_score = 800 + (10 * (rw_correct - 54))
    math_score = 800 + (10 * (math_correct - 44))
    total_score = rw_score + math_score

    row= [rw_score, math_score, total_score]
    scores.append(total_score)
    
    # Write data to csv file
    with open('data.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(row)
        f_object.close()

# Create a histogram by tracking scores per iteration
plt.hist(scores, bins=30, range=(0, 1600), linewidth=0.5, edgecolor="white")

# Set labels and title
plt.xlabel('Total Score')
plt.ylabel('Frequency')
plt.title('Distribution of Total Scores across Iterations')

# Show the plot
plt.show()
