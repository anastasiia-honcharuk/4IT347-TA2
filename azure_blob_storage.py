from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import json

# preprocessing json
def process_json_file(file_path):
    processed_data = []

    with open(file_path, 'r') as file:
        for line in file:
            try:
                json_object = json.loads(line)
                processed_data.append(json_object)
            except json.JSONDecodeError as e:
                print(f"error : {e}")
                continue

    return processed_data

file_path = "yelp.json"
processed_data = process_json_file(file_path)

with open(file_path, 'w') as file:
    json.dump(processed_data, file, indent=2)

print("json file has been reformatted successfully.")

# uploading to azure

connection_string = "DefaultEndpointsProtocol=https;AccountName=nameanastasiia;AccountKey=C/wgcXy6LwCZ8TLxaaW0kQyyGH93t3xwTOIdhVv5oBf5V0vUM4U3JYvYSk2GrdfvAZSTuYYS63D8+AStAmv89w==;EndpointSuffix=core.windows.net"
container_name = "yelp"
blob_name = "yelpdata"  
local_json_file_path = "yelp.json"  

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_client = blob_service_client.get_container_client(container_name)

with open(local_json_file_path, "rb") as data:
    container_client.upload_blob(name=blob_name, data=data)

print(f"uploaded {local_json_file_path} to {container_name}/{blob_name}")
