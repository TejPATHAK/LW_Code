pip install pandas numpy scikit-learn matplotlib seaborn
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    if file_path.endswith('d:\Cognifyz_Internship\Dataset.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('d:\Cognifyz_Internship\Dataset.xlsx') or file_path.endswith('d:\Cognifyz_Internship\Dataset.xls'):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")
    print(f"Dataset loaded successfully with shape: {df.shape}")
    return df

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Fill missing values
    df = df.fillna(df.median(numeric_only=True))  # Fill numeric columns with median
    df = df.fillna(df.mode().iloc[0])  # Fill categorical columns with mode
    
    print("Data cleaned successfully.")
    return df

def preprocess_data(df):
    # Encode categorical variables
    label_encoders = {}
    for column in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le
    
    # Standardize numerical features
    scaler = StandardScaler()
    df[df.select_dtypes(include=[np.number]).columns] = scaler.fit_transform(df.select_dtypes(include=[np.number]))
    
    print("Data preprocessed successfully.")
    return df, label_encoders, scaler

def feature_engineering(df):
    # Example: Create new features (e.g., interaction terms, polynomial features)
    df['new_feature'] = df.iloc[:, 0] * df.iloc[:, 1]  # Interaction between first two columns
    print("Feature engineering completed.")
    return df

def basic_analysis(df):
    # Summary statistics
    print("Summary Statistics:")
    print(df.describe())
    
    # Correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()
    
    # Distribution of features
    df.hist(figsize=(15, 10))
    plt.suptitle("Feature Distributions")
    plt.show()

def process_data(file_path):
    # Step 1: Load the data
    df = load_data(file_path)
    
    # Step 2: Clean the data
    df = clean_data(df)
    
    # Step 3: Preprocess the data
    df, label_encoders, scaler = preprocess_data(df)
    
    # Step 4: Feature engineering
    df = feature_engineering(df)
    
    # Step 5: Basic analysis
    basic_analysis(df)
    
    print("Data processing completed.")
    return df

# Example usage:
# dataset = process_data("your_dataset.csv")
