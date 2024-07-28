import requests
def get_location_from_ip(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    location_data = response.json()
    return location_data