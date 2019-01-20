import json
data = [{"a":"1121", "b":"456"}]
output = json.dumps(data)
print(output)
data1 = '{"first_name":"123","last_name":"456"}'
output1 = json.loads(data1)
print(output1)