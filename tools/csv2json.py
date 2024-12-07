import argparse

parser = argparse.ArgumentParser(description="Process a file.")
parser.add_argument("filename", help="The name of the file to process.")
args = parser.parse_args()
test_json = []
i = 0

with open('csv.json', 'w') as w:
    with open(args.filename, "r") as f:
        for line in f:
            if i > 0:
                details = line.split(',')
                card = {
                    "model": "optcg.card",
                    "pk": i,
                    "fields":{
                        "name": details[0],
                        "market_price": details[1],
                        "rarity": details[2],
                        "desc": details[3],
                        "color": details[4],
                        "cost": details[5]
                    }
                }
                test_json.append(card)
            i += 1
    w.write(str(test_json).replace("'", '"'))