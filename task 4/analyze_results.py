import pandas as pd

# Load CSV data
df = pd.read_csv('results.csv')

# Group by student (name + roll number) and calculate total and average marks
grouped = df.groupby(['name', 'roll_no']).agg(
    total_marks=('marks', 'sum'),
    subjects_count=('subject', 'count')
)

# Calculate percentage
grouped['percentage'] = grouped['total_marks'] / (grouped['subjects_count'] * 100) * 100

# Define grading logic
def get_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

grouped['grade'] = grouped['percentage'].apply(get_grade)

# Reset index for easier saving/display
final_df = grouped.reset_index()

# Sort by percentage descending
sorted_df = final_df.sort_values(by='percentage', ascending=False)

# Display top 5 students
print("Top 5 Students by Percentage:")
print(sorted_df.head(5).to_string(index=False))

# Save final results
sorted_df.to_csv('final_results.csv', index=False)
print("\nAnalyzed results saved to 'final_results.csv'.")
