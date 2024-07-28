import requests
def get_ip_address():
    # Replace this URL with the endpoint used by your vehicle's internet connection
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    return ip_data['ip']
