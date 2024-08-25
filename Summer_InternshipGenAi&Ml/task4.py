import requests

def get_geo_location():
    try:
        # Send a request to the IP info API
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        
        # Extract relevant information
        ip = data.get('ip', 'N/A')
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        loc = data.get('loc', 'N/A').split(',')
        latitude = loc[0] if len(loc) > 0 else 'N/A'
        longitude = loc[1] if len(loc) > 1 else 'N/A'
        
        # Print the results
        print(f"IP Address: {ip}")
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_geo_location()
