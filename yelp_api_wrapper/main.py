from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

with open("yelp.json", "r") as file:
    data = json.load(file)

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
