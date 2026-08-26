import pandas as pd

def Read_data_file(file_path):
    """
    Reads a CSV file and returns a pandas DataFrame.
    """

    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None
    
    
def Drop_unnecessary_features(df, COLS_TO_DROP):
    """
    Drops unnecessary features from a pandas DataFrame.

    """
    return df.drop(columns=COLS_TO_DROP)


def Check_data_type(df):
    report = pd.DataFrame({
        'Data Type': df.dtypes,
        'Unique Values': df.nunique()
        
    })
    
    return report.T

def Handle_and_convert_dtype(df, categorical_cols):
    """
    Converts specified columns in the DataFrame to categorical data type.

    """
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype('category')
        else:
            print(f"Column '{col}' not found in the DataFrame.")
    
    return df

