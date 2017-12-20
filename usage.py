import requests
import json
from tabulate import tabulate
# Raw data courtesy of Allen Guo: https://github.com/guoguo12/hivemind
secret_sauce = 'https://labs.aguo.us/hivemind/data/latest.json'

response = requests.get(url=secret_sauce)
json_object = json.loads(response.text)
data = json_object['data']


#example prints of data
# print(data['hive1.cs']['load_avgs'])
# print data['derby.cs']

#returns a dict / 2d list to be turned into a table
def result():
    return data['derby.cs']
