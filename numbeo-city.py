import requests
from bs4 import BeautifulSoup
import csv
import os

# URL of the website
url = "https://www.numbeo.com/cost-of-living/rankings_current.jsp"

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table with the id 't2'
        table = soup.find('table', {'id': 't2'})

        # Create the 'data' folder if it doesn't exist
        if not os.path.exists('data'):
            os.makedirs('data')

        # Define the file path as a constant
        FILE_PATH = 'data/cost_of_living.csv'

        # Create a CSV file in the 'data' folder to save the data
        with open(FILE_PATH, 'w', newline='') as csvfile:
            # Initialize the CSV writer and write the column headers
            csv_writer = csv.writer(csvfile)
            headers = [
                "City",
                "Cost of Living Index",
                "Rent Index",
                "Cost of Living Plus Rent Index",
                "Groceries Index",
                "Restaurant Price Index",
                "Local Purchasing Index"
            ]
            csv_writer.writerow(headers)

            # Extract table rows and write them to the CSV file
            for row in table.find_all('tr'):
                columns = [col.text.strip() for col in row.find_all('td')]
                if any(columns):
                    csv_writer.writerow(columns[1:])  # Remove the leading comma

        print("Data scraped and saved to 'data/cost_of_living.csv'.")
    else:
        print("Failed to retrieve the webpage.")
except Exception as e:
    print("An error occurred:", str(e))