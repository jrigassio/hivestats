import requests
import json
import re
# Raw data courtesy of Allen Guo: https://github.com/guoguo12/hivemind
secret_sauce = 'https://labs.aguo.us/hivemind/data/latest.json'

response = requests.get(url=secret_sauce)
json_object = json.loads(response.text)
data = json_object['data']

def table():
    usage_matrix = []
    server_list = [str((x, data[x]['load_avgs'][1])) for x in data.keys() if data[x] != {}]
    return "FORMAT: ([Server Name], [CPU Usage (%)])... \n" + (', ').join(server_list)

def least_busy(hive_only=True):
    usage = {}
    if hive_only:
        server_list = [x for x in data.keys() if data[x] != {} and
        not re.match("s[0-9]*-[0-9]*", x) and not re.match("hpse", x) \
        and not re.match("raspi", x)]
    else:
        server_list = [x for x in data.keys() if data[x] != {}]
    for s in server_list:
        pct = data[s]['load_avgs'][1]
        usage[pct] = s
    return usage[sorted(usage)[0]]
