from unidecode import unidecode
from tqdm import tqdm

from urllib.request import urlopen, quote
import json
from datetime import datetime
from datetime import timezone
import sys
import os
import requests

def wikidata_rest_query(query):
    url = "https://query.wikidata.org/sparql?query=%s&format=json" % quote(query)
    with urlopen(url) as f:
        response = f.read().decode("utf-8")
    return json.loads(response)


def buildQuerysingle(sub, pred):
    q = """
    SELECT ?item ?itemLabel (YEAR(?starttime) AS ?yearstarttime) ?endtime WHERE {
        wd:"""+sub +" p:" + pred +""" ?s  .
                ?s  ps:""" + pred +""" ?item .
                ?s  pq:P580 ?starttime  .
                FILTER NOT EXISTS{ ?s pq:P582 ?endtime .}.
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    } order by desc(?starttime)
    """
    return q

def buildQuerysingle_special(sub, pred):
    q = """
  SELECT ?item ?itemLabel (YEAR(?starttime) AS ?yearstarttime) (YEAR(?endtime) AS ?yearendtime) WHERE {
      wd:"""+sub +" p:" + pred +""" ?s  .
            ?s  ps:""" + pred +""" ?item .
            ?s  pq:P580 ?starttime  .
            ?s  pq:P582 ?endtime  .
            FILTER(?endtime>NOW()).
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  } order by desc(?starttime)
  """
    return q

def buildQuerysingle_special2(sub, pred):
    q = """
  SELECT ?item ?itemLabel (YEAR(?starttime) AS ?yearstarttime) ?endtime WHERE {
      wd:"""+sub +" p:" + pred +""" ?s  .
            ?s  ps:""" + pred +""" ?item .
            ?s  pq:P580 ?starttime  .
            ?s  pq:P582 ?endtime  .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  } order by desc(?starttime)
  """
    return q

def buildQueryPrevious(sub, pred):
    q = """
    SELECT ?item ?itemLabel ?starttime ?endtime WHERE {
      wd:"""+sub +" p:" + pred +""" ?s  .
            ?s  ps:""" + pred +""" ?item .
            ?s  pq:P580 ?starttime  .
            ?s pq:P582 ?endtime .
            FILTER(?endtime <=NOW()).
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    } order by desc(?endtime)
    """
    return q


def collect_answers_one_hop(data):
    uid = 8000
    updated_data = dict()
    extra_special=dict()

    """
    data ={
        "Which club does Daichi Kamada currently play for?": {
            "question": "Which club does Daichi Kamada currently play for?",
            "subject": {
                  "subject": "Q20039495",
                  "subLabel": "Daichi Kamada"
            },
            "text answers": [
                  ""
            ],
            "answer annotations": [
                  {
                        "ID": "",
                        "Label": ""
                  }
            ],
            "relations": [
                  "P54"
            ],
            "template": "Which team does {subject} play for currently?",
            "uniq_id": 2297
      },
      "Which team did Daichi Kamada play for last before joining the current team?": {
            "question": "Which team did Daichi Kamada play for last before joining the current team?",
            "subject": {
                  "subject": "Q20039495",
                  "subLabel": "Daichi Kamada"
            },
            "text answers": [
                  ""
            ],
            "answer annotations": [
                  {
                        "ID": "",
                        "Label": ""
                  }
            ],
            "relations": [
                  "P54"
            ],
            "template": "Which team did {subject} play for last before joining the current team?",
            "uniq_id": 7099
      },
      "Which club does Junya Ito currently play for?": {
            "question": "Which club does Junya Ito currently play for?",
            "subject": {
                  "subject": "Q21913126",
                  "subLabel": "Junya Ito"
            },
            "text answers": [
                  ""
            ],
            "answer annotations": [
                  {
                        "ID": "",
                        "Label": ""
                  }
            ],
            "relations": [
                  "P54"
            ],
            "template": "Which team does {subject} play for currently?",
            "uniq_id": 2257
      },
      "Which team did Junya Ito play for last before joining the current team?": {
            "question": "Which team did Junya Ito play for last before joining the current team?",
            "subject": {
                  "subject": "Q21913126",
                  "subLabel": "Junya Ito"
            },
            "text answers": [
                  ""
            ],
            "answer annotations": [
                  {
                        "ID": "",
                        "Label": ""
                  }
            ],
            "relations": [
                  "P54"
            ],
            "template": "Which team did {subject} play for last before joining the current team?",
            "uniq_id": 7097
      }
    }
    """
    

    for k,v in tqdm(data.items()):
      answers = []
      answers_special = []
      sub = k
      pred = v[1]

      #   if 'previous' not in k and 'before' not in k:
      q=buildQuerysingle(sub, pred)
      result_cur = wikidata_rest_query(q)['results']['bindings']
      if len(result_cur) <1 or (len(result_cur)==1 and 'national' in result_cur[0]['itemLabel']['value']):
            q = buildQuerysingle_special(sub, pred)
            result_cur = wikidata_rest_query(q)['results']['bindings']
            
            if len(result_cur) <1 or (len(result_cur)==1 and 'national' in result_cur[0]['itemLabel']['value']):
                  q = buildQuerysingle_special2(sub, pred)
                  results_n = wikidata_rest_query(q)['results']['bindings']
                  # print(results_n)
                  try:
                  
                        if results_n[0]['endtime']['type'] != 'literal':
                              result_cur = [results_n[0]]
                              r=1
                        # print(a['itemLabel']['value'])
                        else:
                              continue
                  except:
                        print(v['subject']['subject'])
                        continue
      text = []
      extra_special_text = []
      for res in result_cur:
            id = res['item']['value'].split('/')[-1]
            label = res['itemLabel']['value']
            answers.append({"ID": id, "Label": label})
            text.append(label)
            # if 2023 - int(res['yearstarttime']['value'] ) >7:
            #     extra_special_text.append(label)
            #     answers_special.append({"ID": id, "Label": label})

      t = "Who is the head of the government of {subject} currently?"
      q = t.replace("{subject}", v[0])
      nitem = {
            "question": q,
            "subject": {
                  "subject": k,
                  "subLabel": v[0]
            },
            "text answers": text,
            "answer annotations": answers,
            "relations": [
                  "P6"
            ],
            "template": "Who is the head of the government of {subject} currently?",
            "uniq_id": uid
      }
      uid+=1
      updated_data[q] = nitem.copy()

      # specialItem = v.copy()
      # specialItem['text answers'] = extra_special_text
      # specialItem['answer annotations'] = answers_special
      # extra_special[k] = specialItem

        
    print(len(updated_data))
    return updated_data, extra_special


def main():
    # if len(sys.argv) == 2:
    #     timestamp = sys.argv[1]
    #     print(f"Received argument: {timestamp}")
    # else:
    #     print("This script requires exactly one argument.")
    #     return
    
    timestamp = 'May2024'
    # dataPath = os.path.join('../PAT-data',timestamp) + '/PAT-singlehop.json'
   
    # if not os.path.exists(dataPath):
    #     print('Data Path does not exist')
    #     return

    # with open(dataPath,'r') as f:
    #     data = json.load(f)
    with open('/Users/jannatarameem/Downloads/PAT_annotation_verify/troubleshooting/why_prev_but_no_cur.json','r') as f:
        data = json.load(f)
    
    print(f'data length: {len(data)}')
    updated_data, extra_special = collect_answers_one_hop(data)
    
    print(f'updated data length: {len(updated_data)}')
    print(f'extra special data length: {len(extra_special)}')
    
    from datetime import datetime

    # Get the current date and time
    now = datetime.now()

    # Extract the current month and year
    current_month = now.strftime("%B")
    current_year = now.year

    # out_path = '../PAT-data/' + current_month + str(current_year)
    out_path = 'test'

    if not os.path.exists(out_path):
        os.makedirs(out_path)
    
    with open(os.path.join(out_path, 'Q_why_prev_but_no_cur.json'),'w') as f:
        json.dump(updated_data,f,indent =6)

    # with open(os.path.join(out_path, 'PAT-singlehop-special-attention.json'),'w') as f:
    #     json.dump(extra_special,f,indent =6)

main()