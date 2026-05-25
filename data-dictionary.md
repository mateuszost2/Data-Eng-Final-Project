| Column | Description | Expected valid values / format |
|---|---|---|
| `Index` | Accidental index column saved in the CSV export. It is not a real analytical attribute and is usually removed during cleaning. | Integer-like row identifier |
| `Pregnancies` | Number of times pregnant. | Numeric, non-negative |
| `Glucose` | Plasma glucose concentration at 2 hours in an oral glucose tolerance test. | Numeric |
| `Blood Pressure` | Diastolic blood pressure (mm Hg). | Numeric |
| `Skin Thickness` | Triceps skin fold thickness (mm). | Numeric |
| `Insulin` | 2-Hour serum insulin (mu U/ml). | Numeric |
| `Body Mass Index` | Body mass index (weight in kg/(height in m)^2). | Numeric |
| `Diabetes Pedigree Function` | Numeric score that summarizes the likelihood of diabetes based on family history. | Numeric |
| `Age` | Age in years. | Numeric, positive |
| `Outcome` | Class variable indicating diabetes outcome. | `0`, `1` |
| `BMI Category` | Derived BMI grouping created from body mass index values. | `underweight`, `normal`, `overweight`, `obese` |
| `Clinic Region` | Derived local categorical field indicating the clinic region associated with the record. | `North`, `South` |
| `Care Path` | Derived local categorical field describing the follow-up pathway for the patient. | `High Risk`, `Routine Follow-up` |
| `Patient Segment` | Derived local categorical field representing an age-based grouping. | `Adult`, `Senior` |
