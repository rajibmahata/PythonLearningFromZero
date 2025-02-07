import json

with open("config.json") as f:
    config = json.load(f)

print(config["api_key"])
