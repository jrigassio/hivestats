import requests
import json
import re
# Raw data courtesy of Allen Guo: https://github.com/guoguo12/hivemind
secret_sauce = 'https://labs.aguo.us/hivemind/data/latest.json'

response = requests.get(url=secret_sauce)
json_object = json.loads(response.text)
data = json_object['data']


#example prints of data
# print(data['hive1.cs']['load_avgs'])
# print data['derby.cs']

#returns a dict or 2d list to be turned into a table
def table():
    usage_matrix = []
    server_list = [x for x in data.keys() if data[x] != {}]
    return server_list

def least_busy(hive_only=True):
    usage = {}
    if hive_only:
        server_list = [x for x in data.keys() if data[x] != {} and
        not re.match("s[0-9]*-[0-9]*", x) and not re.match("hpse", x)]
    else:
        server_list = [x for x in data.keys() if data[x] != {}]
    for s in server_list:
        pct = data[s]['load_avgs'][1]
        usage[pct] = s
    return usage[sorted(usage)[0]]
