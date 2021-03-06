import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def covid_ask(query):
    params = {"query": query, "strat": "dense_first"}
    res = requests.get("https://covidask.korea.ac.kr/api", params=params, verify=False)
    outs = json.loads(res.text)
    return outs


# query = "Is there concrete evidence for the presence of asymptomatic transmissions?"
# results = covidAsk(query)
#
# # Top 10 phrase answers from covidAsk
# print([r['answer'] for r in results['ret']])
