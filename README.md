## Data Engineering Final Project

### 1. Repository setup
- Created GitHub repository with README.md file
- Added `.gitignore` to exclude `.env`

### 2. Docker configuration
- Configured `docker-compose.yml` with MongoDB
- MongoDB runs on `localhost:27017` with credentials stored in `.env`
- `rsc/init.js` creates `diabetes_db` database and `patients` collection on startup


### 3. Data cleaning (data engineer perspective)
- Loaded dirty dataset (`diabetes-dirty.csv`) with `;` separator
- Dropped accidental index column
- Standardized column names (lowercase, underscores)
- Removed units from numerical columns (`mg/dL`, `uU/mL`)
- Normalized casing and whitespace in categorical columns
- Standardized inconsistent categorical labels (e.g. `south-side`→`south`, `normal-weight`→`normal`, `positive`→`1`)
- Replaced invalid string values with `NaN` (e.g. `?`, `nan uU/mL`)
- Replaced biologically impossible values with `NaN` (negative pregnancies, negative BMI)
- Removed duplicate rows
- Added `source_file` column
- Exported cleaned dataset to `diabetes-clean.csv`
### 4. Data ingestion
- Created `MongoDatabase` class for connection management
- Created `MongoExecutor` class for CRUD operations
- Connected to MongoDB using credentials from `.env` using `python-dotenv`
- Mapped each CSV row to a MongoDB document with a generated `external_id`
- Ingested cleaned dataset into `diabetes_db.patients` collection
### 5. Exploratory Data Analysis
- Connected to MongoDB and loaded data into a pandas DataFrame
- Checked shape, types, nulls and duplicates
- Applied data wrangling from a data science perspective: imputed missing values (median/mode), removed outliers
- Added visualizations:
  - Diabetes outcome distribution
  - Glucose levels by outcome boxplot
  - Correlation matrix heatmap
  - BMI category by outcome
  - Pairplot of all numerical features colored by outcome

## How to run
All commands should be run from the project root directory.

```bash
# 1. Start MongoDB
docker compose up -d

# 2. Clean the data
python scripts/cleaning_diabetes_dataset.py

# 3. Ingest into MongoDB
python scripts/ingestion_mongodb.py

# 4. Open EDA notebook
notebooks/eda.ipynb
```