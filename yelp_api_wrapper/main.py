from fastapi import FastAPI, HTTPException
from download_azure import download_json_from_azure
from typing import List 
import re


app = FastAPI()

connection_string = "DefaultEndpointsProtocol=https;AccountName=nameanastasiia;AccountKey=C/wgcXy6LwCZ8TLxaaW0kQyyGH93t3xwTOIdhVv5oBf5V0vUM4U3JYvYSk2GrdfvAZSTuYYS63D8+AStAmv89w==;EndpointSuffix=core.windows.net"
container_name = "yelp"
blob_name = "yelpdata"
data = download_json_from_azure(connection_string, container_name, blob_name)

@app.get("/business")
def read_business(business_id: str, city: str, include_details: bool = False):
    for business in data:
        if business["business_id"] == business_id and business["city"] == city:
            if include_details:
                return business
            else:
                return {
                    "business_id": business["business_id"],
                    "name": business["name"]
                }
    raise HTTPException(status_code=404, detail="Business not found.")

@app.get("/search")
def search_businesses(city: str):
    matching_businesses = []
    for business in data:
        print(business["categories"])
        restaurant = re.search(r'restaurants', str(business["categories"]), re.IGNORECASE)
        if restaurant and \
            (city is None or business["city"] == city):
            matching_businesses.append(business)
    if not matching_businesses:
        raise HTTPException(status_code=404, detail="No businesses found")
    return matching_businesses
