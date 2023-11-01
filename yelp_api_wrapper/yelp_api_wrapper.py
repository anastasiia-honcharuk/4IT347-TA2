import requests

class YelpAPIWrapper:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_business(self, business_id, city, include_details=False):
        url = f"{self.base_url}/business"
        params = {
            "business_id": business_id,
            "city": city,
            "include_details": include_details
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get business information: {response.status_code} - {response.text}")
