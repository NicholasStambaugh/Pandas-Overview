import pandas as pd

df = pd.DataFrame([
    ['Name', 'Age', 'City', 'Weight', 'Height', 'Gender'],
    ['John', 25, 'New York', 70, 180, 'Male'],
    ['Alice', 30, 'London', 65, 165, 'Female'],
    ['Bob', 35, 'Paris', 80, 175, 'Male'],
    ['Emma', 28, 'Los Angeles', 60, 170, 'Female'],
    ['Michael', 40, 'Berlin', 85, 190, 'Male'],
    ['Sophia', 32, 'Tokyo', 55, 160, 'Female'],
    ['David', 45, 'Sydney', 75, 175, 'Male'],
    ['Olivia', 27, 'Toronto', 68, 168, 'Female'],
    ['Daniel', 38, 'Moscow', 90, 180, 'Male']
])

# Display the first 5 rows of the dataframe
print(df.head())

# Display the shape of the dataframe
print(df.shape)

# Display the column names of the dataframe
print(df.columns)

# Display the summary statistics of the dataframe
print(df.describe())

# Filter the dataframe based on a condition
filtered_df = df[df['Age'] > 30]
print(filtered_df)

# Example: Calculate the mean of the 'Age' column
mean_age = df['Age'].mean()
print("Mean Age:", mean_age)

# Example: Group the data by 'Gender' and calculate the sum of 'Weight'
grouped_df = df.groupby('Gender')['Weight'].sum()
print(grouped_df)

# Example: Merge two dataframes based on a common column
df1 = pd.DataFrame({'column_name': [1, 2, 3], 'another_column': ['A', 'B', 'C']})
df2 = pd.DataFrame({'column_name': [2, 3, 4], 'additional_column': ['X', 'Y', 'Z']})
merged_df = pd.merge(df1, df2, on='column_name')
print(merged_df)

# Group the dataframe by 'Gender' and calculate the mean of 'Age'
grouped_df = df.groupby('Gender')['Age'].mean()
print(grouped_df)

# Sort the dataframe by 'Age' in ascending order
sorted_df = df.sort_values('Age')
print(sorted_df)

# Create a new column 'BMI' in the dataframe
df['BMI'] = df['Weight'] / (df['Height'] ** 2)
print(df)

# Calculate the median of the 'Age' column
median_age = df['Age'].median()
print("Median Age:", median_age)

# Calculate the maximum value of the 'Weight' column
max_weight = df['Weight'].max()
print("Max Weight:", max_weight)

# Calculate the minimum value of the 'Height' column
min_height = df['Height'].min()
print("Min Height:", min_height)

# Count the number of unique values in the 'Gender' column
unique_genders = df['Gender'].nunique()
print("Unique Genders:", unique_genders)

# Drop rows with missing values
cleaned_df = df.dropna()
print(cleaned_df)

