from Config.config import DATA_PATH, COLS_TO_DROP, CATEGORICAL_COLS
from preprocessing import (
    Read_data_file,
    Drop_unnecessary_features,
    Check_data_type,
    Handle_and_convert_dtype,
)


def main():
    # 1. Read the dataset
    df = Read_data_file(DATA_PATH)

    if df is not None:
        # 2. Display initial report
        print("--- Initial Data Quality Report ---")
        print(Check_data_type(df))

        # 3. Drop unnecessary features
        df_cleaned = Drop_unnecessary_features(df, COLS_TO_DROP)

        # 4. Convert categorical columns data type
        df_converted = Handle_and_convert_dtype(df_cleaned, CATEGORICAL_COLS)

        # 5. Display final data quality report
        print("\n--- Cleaned & Converted Data Quality Report ---")
        print(Check_data_type(df_converted))


if __name__ == "__main__":
    main()