import pandas as pd

data = {
    'Column 1': ['A', 'D', 'I', 'X', 'I', 'N', 'Q'],
    'Column 2': ['B', 'E', 'J', 'Y', 'M', 'O', 'S'],
    'Column 3': ['Type A', 'Type A', 'Type A', 'Type B', 'Type B', 'Type B', 'Type B']
}

df = pd.DataFrame(data)

def replace_column_values(df):

    # Loop through each unique category in 'Column 3'
    for category in df['Column 3'].unique():
        # Create a boolean mask (a series of true and false values) that identifies 
        # which rows in Column 3 match the current category being processed. 
        # This mask is used to filter the DataFrame for that specific category.
        mask = df['Column 3'] == category
        
        # Check if there are more than one entries in the current category by summing the True values in the mask. 
        if mask.sum() > 1:
            # Extract the relevant rows -> Filters the original DataFrame df using the boolean mask 
            # to create a new DataFrame group that contains only the rows belonging to the current category.
            group = df[mask]
            
            # group.index[:-1]  ->  select all indices of the group DataFrame except the last one (this is because I want to avoid modifying the last entry).
            # group['Column 1'].values[1:] ->  retrieve all but the first value of Column 1 within the current group. 
            # This effectively shifts the values of Column 1 down one position to replace Column 2 (except the last value of Column 2, which remains unchanged).
            df.loc[group.index[:-1], 'Column 2'] = group['Column 1'].values[1:]
    
    # Return the modified DataFrame df with the updated values in Column 2.
    return df

# Call the function with the DataFrame df as an argument, storing the resulting modified DataFrame in output_df.
output_df = replace_column_values(df)
print(output_df)
