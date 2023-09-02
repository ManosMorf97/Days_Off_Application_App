import json

dict1={'name':'Manos','parents':['MILTOS','SOULA']}
json_d=json.dumps(dict1)
print(json_d)
json_l=json.loads(json_d)
print(json_l)