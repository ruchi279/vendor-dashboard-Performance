Vendor Performance Analysis Dashboard
Overview

This project analyzes vendor performance using inventory, purchase, and invoice data. The goal is to provide actionable insights into vendor efficiency, inventory management, purchasing trends, and business performance through data analysis and visualization.

Features
Data ingestion and processing using Python
Exploratory Data Analysis (EDA)
Vendor performance evaluation
Inventory analysis
Purchase and pricing trend analysis
Interactive dashboard for visualization
Business insights and recommendations
Dataset

The project uses the following datasets:

begin_inventory.csv
end_inventory.csv
purchases.csv
purchase_prices.csv
vendor_invoice.csv

These datasets contain information related to inventory levels, purchases, pricing, and vendor transactions.

Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
SQLite
Jupyter Notebook
HTML
GitHub Pages
Project Structure
vendor-dashboard-Performance/
│
├── Exploratory Data Analysis.ipynb
├── Vendor Performance Analysis.ipynb
├── ingestion_db.py
├── get_vendor_summary.py
├── index.html
├── begin_inventory.csv
├── end_inventory.csv
├── purchase_prices.csv
├── vendor_invoice.csv
└── README.md
Key Insights
Identified top-performing vendors based on sales and profitability.
Analyzed inventory turnover and stock movement.
Examined purchase patterns and vendor contributions.
Generated data-driven recommendations for vendor management.
Dashboard Preview

The dashboard presents:

Vendor-wise performance metrics
Inventory statistics
Purchase trends
Pricing analysis
Interactive visualizations
How to Run
Clone the repository:
git clone https://github.com/ruchi279/vendor-dashboard-Performance.git
Install dependencies:
pip install pandas numpy matplotlib seaborn
Run the data ingestion script:
python ingestion_db.py
Open the Jupyter notebooks for analysis:
jupyter notebook

Future Improvements
-Real-time data updates
-Advanced machine learning predictions
-Vendor ranking system
-Interactive filtering and reporting

Author
Ruchi Singh
