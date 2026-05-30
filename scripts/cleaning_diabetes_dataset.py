import pandas as pd
import numpy as np
from pathlib import Path

## change pandas option to always display all collumns
pd.set_option('display.max_columns', None)

## define clean and dirty paths
DIRTY_PATH = Path("raw/diabetes/diabetes-dirty.csv")
CLEAN_PATH = Path("raw/diabetes/diabetes-clean.csv")

## create dataframe for cleaning
df = pd.read_csv(DIRTY_PATH, sep=';')

## remove unnecessary columns
df.drop(columns=['Unnamed: 0'], inplace=True)

## standardize column names
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

numerical_cols = ['pregnancies', 'glucose', 'blood_pressure', 'skin_thickness',
                  'insulin', 'body_mass_index', 'diabetes_pedigree_function', 'age']

categorical_cols = ['outcome', 'bmi_category', 'clinic_region', 'care_path', 'patient_segment']

## standardize unique values in numerical columns

# pregnancies
df['pregnancies'] = df['pregnancies'].where(df['pregnancies'] >= 0, np.nan)
df['pregnancies'] = df['pregnancies'].astype('Int64')

# glucose
df['glucose'] = df['glucose'].str.replace('mg/dL', '').str.replace('?', '').str.strip()
df['glucose'] = df['glucose'].replace('', np.nan).replace('nan', np.nan)
df['glucose'] = df['glucose'].astype('float64')

# blood_pressure - looks okay
# print(df['blood_pressure'].unique().tolist()) correct

# skin_thickness - looks okay
# print(df['blood_pressure'].unique().tolist())

# insulin
df['insulin'] = df['insulin'].str.replace('uU/mL', '').str.replace('?', 'nan').str.strip()
df['insulin'] = df['insulin'].replace({'': np.nan, 'nan': np.nan}).astype('float64')

# body_mass_index
df['body_mass_index'] = df['body_mass_index'].str.replace('bmi', '').str.replace('?', 'nan').str.strip()
df['body_mass_index'] = df['body_mass_index'].replace({'': np.nan, 'nan': np.nan}).astype('float64')
df['body_mass_index'] = df['body_mass_index'].where(df['body_mass_index'] >= 0, np.nan)

# diabetes_pedigree_function - looks okay

# age
df['age'] = df['age'].str.replace('years', '').str.strip().astype('float64')
df['age'] = df['age'].where(df['age'] >= 0, np.nan)
df['age'] = df['age'].where(df['age'] < 150, np.nan)

## standardize unique values in categorical columns

# outcome
df['outcome'] = df['outcome'].str.replace('?', 'nan').str.strip()
df['outcome'] = df['outcome'].replace({'positive': '1', 'negative': '0', 'nan': np.nan}).astype('Int64')

# bmi_category
df['bmi_category'] = df['bmi_category'].str.lower().str.strip()
df['bmi_category'] = df['bmi_category'].replace(
    {'normal-weight': 'normal', 'under wt': 'underweight', 'nan': np.nan, 'unknown': np.nan, })

# clinic_region
df['clinic_region'] = df['clinic_region'].str.lower().str.strip()
df['clinic_region'] = df['clinic_region'].replace(
    {'south-side': 'south', 'n': 'north', '?': np.nan, 'unknown': np.nan, })

# care_path
df['care_path'] = df['care_path'].str.lower().str.strip().str.replace(' ', '-')
df['care_path'] = df['care_path'].replace({'urgent-monitoring': 'high-risk', 'routine': 'routine-follow-up'})

# patient_segment
df['patient_segment'] = df['patient_segment'].str.lower().str.strip().str.replace(' ', '-')
df['patient_segment'] = df['patient_segment'].replace({'mid-age': 'adult', '?': np.nan}, )

## fill missing values

# use median for numerical columns
for col in numerical_cols:
    df[col] = df[col].fillna(df[col].median())

# use mode for categorical columns
for col in categorical_cols:
    if df[col].mode().empty:
        df[col] = df[col].fillna("unknown")
    else:
        df[col] = df[col].fillna(df[col].mode()[0])


## remove outlayers
df = df[df['glucose'] <= 500]
df = df[df['insulin'] <= 1000]
df = df[df['body_mass_index'] <= 70]

## remove duplicated columns
df = df.drop_duplicates()



## add source path column to data frame
df['source_file'] = 'diabetes-dirty.csv'

## final datatype conversions
df['glucose'] = df['glucose'].astype('Int64')
df['blood_pressure'] = df['blood_pressure'].astype('Int64')
df['skin_thickness'] = df['skin_thickness'].astype('Int64')
df['insulin'] = df['insulin'].astype('Int64')
df['age'] = df['age'].astype('Int64')

df.to_csv(CLEAN_PATH, index=False)