import pandas as pd

# Load the first Excel file into a DataFrame
df1 = pd.read_excel('list1.xlsx')

# Load the second Excel file into another DataFrame
df2 = pd.read_excel('list2.xlsx')

# Extract email IDs from both DataFrames
emails_df1 = set(df1['emailid'])
emails_df2 = set(df2['emailid'])

# Find common email IDs
common_emails = emails_df1.intersection(emails_df2)

# Remove rows with common email IDs from both DataFrames
df1 = df1[~df1['emailid'].isin(common_emails)]
df2 = df2[~df2['emailid'].isin(common_emails)]

# Concatenate the two DataFrames without common email IDs
result_df = pd.concat([df1, df2])

# Save the result to a new CSV file
result_df.to_csv('result.csv', index=False)