# Replace Column Project

## Environment Setup

### 1. Select Python Interpreter

To ensure compatibility with the project, please select Python 3.x as your interpreter. This can typically be done in your IDE (e.g., VSCode) by navigating to the interpreter settings and selecting the appropriate version from the list.

On VSCode, use ctrl+shift+P to select Python Interpreter.

```cmd
pip install -r requirements.txt
```

### 2. Install Required Packages

Before running the project, make sure to install the necessary packages. You can do this by executing the following command in your terminal or command prompt:

To run the requirements, use the following command:

```cmd
pip install -r requirements.txt
```

To run the scripts, use the IDE's run functionality or use the following command:

```cmd
python .\scripts\replace_column_values.py
```

## My Thought Process

### 1. **Understand the Problem Requirements**

The first step, I carefully reviewed the problem description and identified the key operations required

- The goal was to replace the values in **Column 2** using values from **Column 1**, grouped by the category in **Column 3**.
- Special attention was needed to ensure that the last value for each category in **Column 2** remains unchanged.

### 2. **Plan the Approach**

Once the requirements were clear, I planned how to implement the solution

1. **Group by category**
   Since **Column 3** defines the categories, the first task was to group rows by the unique values in this column.
2. **Shift values**
   For each group, the values in **Column 2** should be replaced by values from **Column 1**, starting from the second value.
3. **Exclude the last value**
   The challenge here was to modify only the first entries of each group, while keeping the last value intact.

### 3. **Choose the Tools**

I decided to use the Pandas library which is a data manipulation and analysis tool in Python to handle the DataFrame manipulations, as it provides powerful capabilities for vectorized operations, grouping, and conditional indexing. It is commonly used for working with structured data in the form of DataFrames, which are two-dimensional and size-mutable.

### Step 4: **Implement the Solution**

I broke down the problem into the following implementation steps:

1. **Create the DataFrame**
   First, I created a sample DataFrame that reflects the structure of the input data that contains three key-value pairs. Each key represents a column name, and the associated value is a list of entries for that column.
   - Column 1 contains letters that serve as identifiers.
   - Column 2 contains associated letters that will be modified.
   - Column 3 categorizes the data into two types: Type A and Type B
2. **Iterate over categories**
   Using Pandas, I looped over the unique values in **Column 3** to process each category separately.
3. **Replace the values in Column 2**
   For each category, I used a mask to select the relevant rows and shifted the values from **Column 1** into **Column 2** using `.loc[]` for assignment ensuring there are no mismatches in lengths. The slicing `[:-1]` ensured that the last value for each group remained unchanged.
4. **Handle edge cases**
   I ensured that categories with only one entry are not modified, since there is no second value to shift.

### Step 5: **Refine the Code**

Finally, I refactored the code into a function to make it reusable and structured. I also made sure the solution avoided chained assignments (which can cause performance issues or warnings in Pandas) by using `.loc[]` for direct manipulation of the DataFrame.

### Step 6: **Test the Solution**

I tested the solution with the provided sample data to ensure it met the requirements. I also considered edge cases, such as categories with only one row, to make sure the function handled those cases appropriately.

## Testing

This project includes unit tests to ensure the reliability of the `replace_column_values` function. The tests are located in the `tests/` directory and utilize the `unittest` framework. The testing process involves:

1. **Setup**: A sample DataFrame is created to serve as input for testing.
2. **Execution**: The `replace_column_values` function is called with the test DataFrame.
3. **Validation**: The output is compared against an expected DataFrame to verify correctness.

To run the tests, use the IDE's run functionality or use the following command:

```cmd
python .\tests\test_replace_column_values.py
or
python -m unittest .\tests\test_replace_column_values.py

```

## Visualization

To run the visualizations, use the IDE's run functionality or use the following command:

```cmd
python .\visualizations\visual_replace_column_values.py
```
