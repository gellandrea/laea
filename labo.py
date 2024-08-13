import os
import pandas as pd

def main(path, file_list):
    # Create a list to store the dataframes
    dfs = []

    # Iterate over the file names in file_list
    for file_name in file_list:
        # Create the complete file path using os.path.join()
        file_path = os.path.join(path, file_name)

        # Read the CSV file into a dataframe
        df = pd.read_csv(file_path)

        # Append the dataframe to the list
        dfs.append(df)

    # Perform operations on the dataframes or return the list of dataframes

    return dfs

# Example usage
path = "/path/to/data_folder"
file_list = ["data1.csv", "data2.csv", "data3.csv"]
df_fin = main(path, file_list)
