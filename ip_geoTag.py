import csv
from ip2geotools.databases.noncommercial import DbIpCity

# Function to get country and state information for an IP address
def get_location(ip_address):
    try:
        response = DbIpCity.get(ip_address, api_key='free')
        country = response.country
        state = response.region
        city = response.city
        return country, state, city
    except Exception as e:
        print(f"Error processing IP address {ip_address}: {e}")
        return None, None

# Read the input CSV file
input_file = 'file.csv'
output_file = 'output2.csv'

with open(input_file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    rows = list(reader)

# Process IP addresses and retrieve location information
results = []
for row in rows:
    ip_address = row[0]
    country, state, city = get_location(ip_address)
    results.append([ip_address, country, state, city])

# Write the results to a new CSV file
with open(output_file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(results)

print("IP geolocation process completed. Results saved in", output_file)
