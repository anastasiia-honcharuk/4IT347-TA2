from yelp_api_wrapper import YelpAPIWrapper

# Define the base URL of your FastAPI application
base_url = "http://127.0.0.1:8000"  # Replace with your FastAPI server's URL

# Create an instance of the YelpAPIWrapper
yelp_api = YelpAPIWrapper(base_url)

# Example: Get business information by ID and city
business_id = "Pns2l4eNsfO8kk83dixA6A"
city = "Santa Barbara"
include_details = True

try:
    business_info = yelp_api.get_business(business_id, city, include_details)
    print("Business Information:")
    print(business_info)
except Exception as e:
    print(f"Error: {e}")
