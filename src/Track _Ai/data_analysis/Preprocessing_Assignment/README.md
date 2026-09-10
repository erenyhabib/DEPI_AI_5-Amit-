# Titanic Data Preprocessing Pipeline

A modular, reusable, and configuration-driven Python data preprocessing pipeline built with `pandas`. This project demonstrates solid software engineering best practices for building scalable data pipelines ready for machine learning workflows.

---

## 🛠️ Project Features

- **Modular & Clean Architecture**: Functions are separated into logical scripts for maintainability.
- **Configuration-Driven**: Dataset-specific parameters (such as path and column names) are decoupled from the preprocessing logic.
- **Robust Error Handling**: Safely reads files and validates column existence before execution.
- **Data Quality Reporting**: Generates transposed, readable data summaries including data types and unique value counts.


🧩 Pipeline Components
1-Read_data_file(file_path): Safely loads the dataset into a pandas DataFrame with error handling for invalid paths.

2-Check_data_type(df): Generates a quick data quality report showing column names, dtypes, and unique value counts.

3-Drop_unnecessary_features(df, cols_to_drop): Removes specified redundant columns dynamically.

4-Handle_and_convert_dtype(df, categorical_cols): Converts categorical features to pandas category dtype safely.

## 📊 Pipeline Output

Here is the sample console output generated when executing `Main.py`:
<img width="1388" height="333" alt="Screenshot 2026-08-26 141606" src="https://github.com/user-attachments/assets/451e05c9-852f-4469-8d23-7717327957db" />
