import json
from datetime import datetime
from elasticsearch import Elasticsearch

# Initialize the Elasticsearch client
es = Elasticsearch(hosts=["http://localhost:9200"])

# Open the file test.json
with open("test.json", "r") as f:
    # Load the data from the file into a variable
    data = json.load(f)
    # Iterate over the data
    for d in data:
        # Convert the @timestamp field to the correct format
        d["@timestamp"] = datetime.strptime(d["@timestamp"], "%Y-%m-%d").isoformat()
        # Send the data to Elasticsearch
        es.index(index='my_index', body=d, id=d["@timestamp"])

# Close the file
f.close()
