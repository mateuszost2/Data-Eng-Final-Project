## Data Engineering Final Project

### 1. Repository setup
- Created GitHub repository with README.md file
- Added `.gitignore` to exclude `.env`

### 2. Docker configuration
- Configured `docker-compose.yml` with MongoDB
- MongoDB runs on `localhost:27017` with credentials stored in `.env`

### 3. Data cleaning (data engineer perspective)
- Loaded dirty dataset (`diabetes-dirty.csv`) with `;` separator
- Dropped accidental index column
- Standardized column names (lowercase, underscores)
- Removed units from numerical columns (`mg/dL`, `uU/mL`)
- Normalized casing and whitespace in categorical columns
- Replaced invalid string values with `NaN` (e.g. `?`, `nan`)
- Replaced biologically impossible values with `NaN` (negative pregnancies)
- Removed duplicate rows
- Added `source_file` column
- Exported cleaned dataset to `diabetes-clean.csv`
### 4. Data ingestion
- Created `MongoDatabase` class for connection management
- Created `MongoExecutor` class for CRUD operations
- Connected to MongoDB using credentials from `.env` using `python-dotenv`
- Mapped each CSV row to a MongoDB document with a generated `external_id`
- Ingested cleaned dataset into `diabetes_db.patients` collection