from yelp_api_wrapper import YelpAPIWrapper

# fastapi server url
base_url = "http://127.0.0.1:8000"

yelp_api = YelpAPIWrapper(base_url)

#test
#business_id = "Pns2l4eNsfO8kk83dixA6A"
#city = "Santa Barbara"
include_details = True

#try:
#    business_info = yelp_api.get_business(business_id, city, include_details)
#    print("Business Information:")
#    print(business_info)
#except Exception as e:
#    print(f"Error: {e}")

city = "Philadelphia"
postal_code = "10000"
categories=["Restaurants"]

try:
    business_info = yelp_api.search_businesses(city)
    print("Business Information:")
    print(business_info)
except Exception as e:
    print(f"Error: {e}")