Web Scraping - Largest US Companies by Revenue
This project is a simple web scraping script in Python that extracts the table of the largest companies in the United States by revenue from Wikipedia.

The extracted data is processed into a Pandas DataFrame and then exported to a CSV file for further use.

📄 Project Description
Source Website: Wikipedia - List of Largest US Companies by Revenue

Objective: Scrape the main table containing the list of companies and export it into a structured CSV file.

🛠️ Technologies Used
Python 3+

Libraries: requests, pandas, BeautifulSoup

🚀 How to Run the Project
Clone this repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Install the required libraries (if not already installed):
pip install requests pandas beautifulsoup4


Run the Python script:
WebScraping.py

After scraping, the data will be saved to a CSV file.
Important:
Please make sure to change the path in the script where the DataFrame is exported to a CSV file to match your local system.
Example:
# Change this path as per your local machine
df.to_csv('C:/your-folder/companies.csv', index=False)


📊 Output
The output CSV file will contain structured data with columns such as:

Rank  
Name  
Industry  
Revenue  
Profit  
Employees  
Headquarters


⚡ Notes
The Wikipedia page structure may change over time, which could require updating the scraping logic.

Always be respectful and follow web scraping best practices.

📬 Contact
If you have any questions or suggestions, feel free to open an issue or reach out!
