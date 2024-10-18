import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Column 1': ['A', 'D', 'I', 'X', 'I', 'N', 'Q'],
    'Column 2': ['B', 'E', 'J', 'Y', 'M', 'O', 'S'],
    'Column 3': ['Type A', 'Type A', 'Type A', 'Type B', 'Type B', 'Type B', 'Type B']
}

df = pd.DataFrame(data)

def replace_column_values(df):
    for category in df['Column 3'].unique():
        mask = df['Column 3'] == category
        
        if mask.sum() > 1:

            group = df[mask]
            
            df.loc[group.index[:-1], 'Column 2'] = group['Column 1'].values[1:]
    
    return df

def plot_table_comparison(original_df, modified_df):
    comparison_df = pd.DataFrame({
        'Column 1': original_df['Column 1'],
        'Original Column 2': original_df['Column 2'],
        'Modified Column 2': modified_df['Column 2'],
        'Column 3': original_df['Column 3']
    })

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_frame_on(False)

    table = ax.table(cellText=comparison_df.values, colLabels=comparison_df.columns, cellLoc='center', loc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    plt.show()

original_df = df.copy()

modified_df = replace_column_values(df)

plot_table_comparison(original_df, modified_df)
