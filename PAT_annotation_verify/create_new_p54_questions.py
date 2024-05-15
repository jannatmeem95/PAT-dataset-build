import json

from urllib.request import urlopen, quote
import json
from datetime import datetime
from datetime import timezone
import sys
import os
import requests


with open(
    "/home/jmeem001/Desktop/PAT-extension/May13/insert_new_questions_p54_ids.json", "r"
) as f:
    ids = f.readlines()
ids = [int(x.strip()) for x in ids]

with open("/home/jmeem001/Desktop/PAT-extension/May13/p54_new_questions.txt", "r") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

with open("/home/jmeem001/Desktop/PAT-extension/May13/p54_special_231.json", "r") as f:
    special_p54 = json.load(f)

i = 0


def wikidata_rest_query(query):
    url = "https://query.wikidata.org/sparql?query=%s&format=json" % quote(query)
    with urlopen(url) as f:
        response = f.read().decode("utf-8")
    return json.loads(response)


def get_label(id):
    q = (
        """
    SELECT ?label WHERE {
    wd:"""
        + id
        + """ rdfs:label ?label .
    FILTER(LANG(?label) = "en")
    }
    """
    )
    return wikidata_rest_query(q)["results"]["bindings"][0]["label"]["value"]


t = "Which team did {subject} play for last before joining the current team?"
modified = dict()
uid = 7000
for k, v in special_p54.items():
    if v["uniq_id"] in ids:
        q = lines[i].split("(")[0]
        sid = lines[i].split("(")[1]
        label = get_label(sid)

        i += 1
        n = {
            "question": q,
            "subject": {"subject": sid, "subLabel": label},
            "text answers": [""],
            "answer annotations": [{"ID": "", "Label": ""}],
            "relations": ["P54"],
            "template": v["template"],
            "uniq_id": v["uniq_id"],
        }

        modified[q] = n.copy()

        q2 = t.replace("{subject}", label)
        n2 = {
            "question": q2,
            "subject": {"subject": sid, "subLabel": label},
            "text answers": [""],
            "answer annotations": [{"ID": "", "Label": ""}],
            "relations": ["P54"],
            "template": t,
            "uniq_id": uid,
        }
        uid += 1
        modified[q2] = n2.copy()

        # print(q)
        # print(modified[q])

    else:
        modified[k] = v

print(f"length: {len(modified)}")
with open("test/test.json", "w") as f:
    json.dump(modified, f, indent=6)
