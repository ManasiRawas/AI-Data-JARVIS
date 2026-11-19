# AI Data Analyst JARVIS

### Interactive Data Analytics Dashboard Using Python

AI Data Analyst JARVIS is a web-based analytics application that allows users to upload CSV datasets and explore them through dataset previews, missing-value analysis, descriptive statistics, and interactive visualizations.

## Features

- Upload CSV datasets
- Preview dataset records
- Display row and column counts
- List dataset columns
- Analyze missing values
- Generate interactive Plotly charts for supported HR dataset columns
- View descriptive statistics
- Download the uploaded dataset as CSV

## Technology Stack

- Python
- Pandas
- NumPy
- Streamlit
- Plotly

## Project Structure

```text
AI-Data-JARVIS/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── aug_train.csv
│   ├── aug_test.csv
│   └── sample_submission.csv
└── reports/
```

The local virtual environment (`venv/`) is excluded from version control.

## Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/ManasiRawas/AI-Data-JARVIS.git
   cd AI-Data-JARVIS
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   streamlit run app.py
   ```

Open http://localhost:8501 in your browser.

## Included Dataset

The `data/` directory contains HR analytics CSV files: `aug_train.csv`, `aug_test.csv`, and `sample_submission.csv`. The application also accepts other CSV files; visualizations are displayed when their expected columns are present.

## Future Improvements

- Natural-language AI analysis
- Automated data cleaning and preprocessing
- Additional visualizations
- Machine-learning model integration
- Exportable analytical reports

## Author

**Manasi Rawas**

- GitHub: https://github.com/ManasiRawas
- LinkedIn: https://linkedin.com/in/manasi-rawas-analytics
- Repository: https://github.com/ManasiRawas/AI-Data-JARVIS

---
Built with Python, Pandas, Streamlit, and Plotly.
