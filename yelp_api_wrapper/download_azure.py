from azure.storage.blob import BlobServiceClient
import json

def download_json_from_azure(connection_string, container_name, blob_name):
    try:
        # Create a BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # Get the Azure Blob client
        blob_client = blob_service_client.get_blob_client(container_name, blob_name)

        # Download the JSON data from Azure
        json_data = blob_client.download_blob()
        content = json_data.readall()

        # Decode the content to a string
        content_str = content.decode("utf-8")

        # Parse the decoded content as JSON
        azure_data = json.loads(content_str)

        return azure_data
    except Exception as e:
        print(f"An error occurred while downloading JSON from Azure: {e}")
        return None

# usage
connection_string = "DefaultEndpointsProtocol=https;AccountName=nameanastasiia;AccountKey=C/wgcXy6LwCZ8TLxaaW0kQyyGH93t3xwTOIdhVv5oBf5V0vUM4U3JYvYSk2GrdfvAZSTuYYS63D8+AStAmv89w==;EndpointSuffix=core.windows.net"
container_name = "yelp"
blob_name = "yelpdata"  
azure_data = download_json_from_azure(connection_string, container_name, blob_name)

# test
#if azure_data is not None:
#    print("Azure JSON Data:")
#    print(azure_data)
