## Data Engineering Final Project

### 1. Repository setup
- Created GitHub repository with README.md file
- Added `.gitignore` to exclude `.env`

### 2. Docker configuration
- Configured `docker-compose.yml` with MongoDB
- MongoDB runs on `localhost:27017` with credentials stored in `.env`

### 3. Data cleaning
- Loaded dirty dataset (`diabetes-dirty.csv`) with `;` separator
- Dropped accidental index column
- Standardized column names (lowercase, underscores)
- Cleaned numerical columns: removed units (`mg/dL`, `uU/mL`), standardized missing values
- Cleaned categorical columns: normalized casing, removed whitespace, standarized inconsistent labels
- Replaced biologically impossible values with `NaN` (negative pregnancies)
- Removed obvious outliers (glucose > 500, insulin > 1000, BMI > 70, age > 120)
- Imputed missing values: median for numerical columns, mode for categorical columns
- Removed duplicate rows
- Added `source_file` column
- Exported cleaned dataset to `diabetes-clean.csv`
