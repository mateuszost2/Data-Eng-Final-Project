from textwrap import indent

import pandas as pd
import numpy as np
from pathlib import Path

from fontTools.subset import prune_features

# change pandas option to always display all collumns
pd.set_option('display.max_columns', None)

# define clean and dirty paths
DIRTY_PATH = Path("../raw/diabetes/diabetes-dirty.csv")
CLEAN_PATH = Path("../raw/diabetes/diabetes-clean.csv")

# create dataframe for cleaning
df = pd.read_csv(DIRTY_PATH, sep=';')

# remove unnecessary columns
df.drop(columns=['Unnamed: 0'], inplace=True)

# standardize column names
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

numerical_cols = ['pregnancies', 'glucose', 'blood_pressure', 'skin_thickness',
                  'insulin', 'body_mass_index', 'diabetes_pedigree_function', 'age']

categorical_cols = ['outcome', 'bmi_category', 'clinic_region', 'care_path', 'patient_segment']

# standardize unique values in numerical columns

# pregnancies
df['pregnancies'] = df['pregnancies'].where(df['pregnancies'] >= 0, np.nan)
df['pregnancies'] = df['pregnancies'].astype('Int64')

# glucose
df['glucose'] = df['glucose'].str.replace('mg/dL', '').str.replace('?', '').str.strip()
df['glucose'] = df['glucose'].replace('', np.nan).replace('nan', np.nan)
df['glucose'] = df['glucose'].astype('float64')

# blood_pressure
print(df['blood_pressure'].unique().tolist())

#print(df.dtypes)
