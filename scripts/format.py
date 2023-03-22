import json

entities = json.loads(open("./registry/data/meme/meme-1/contracts.json").read())
sorted_entities = sorted(entities, key=lambda k: k["name"])

json.dump(sorted_entities, open("./registry/data/meme/meme-1/contracts.json", "w"), indent=2)
