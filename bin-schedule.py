import requests
from bs4 import BeautifulSoup

BIN_SCHEDULE_URL = "https://forms.rbwm.gov.uk/bincollections?uprn=10012307006"

response = requests.get(BIN_SCHEDULE_URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find("table")
    rows = table.find_all('tr')[1:]
    next_collection = rows[0]
    service = next_collection.find_all('td')[0].text.strip()
    date = next_collection.find_all('td')[1].text.strip()

    print(f"Next bin collection: {service} on {date}")

