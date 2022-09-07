from collections.abc import MutableMapping

def flatten_dict(input_dict, parent_key = '', seperator = '.'):
    items = []
    for k, v in input_dict.items():
        new_key = str(parent_key) + seperator + k if parent_key else k
        
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, seperator).items())
            
        elif isinstance(v, list):
            for key, value in enumerate(v):
                items.extend(flatten_dict({str
                (key): value}, new_key).items())
        
        else:
            items.append((new_key, v))
    
    return dict(items)

# def getChanges(object_input1, object_input1):
object_input1 = { "someKey":1,
  "secondKey" :{ "first":"hello", "second":"world" }
}
object1 = flatten_dict(object_input1)

object_input2 = { "someKey":1,
  "secondKey" :{ "first":"HELLO",
                          "second":"WORLD"
      }
}
object2 = flatten_dict(object_input2)

# print(object1)
# print("-----", object2)

res = []

for key, value in object2.items():
    print(key)
    if key in object1:
        # print(key)
        if value != object1[key]:
            res.append({key: {str(object1[key])+" is changed to "+value}})
    else:
        res.append({key: {str(key)+" is not present in object1"}})
    
for key, value in object1.items():
    if key not in object2.keys():
        res.append({key: {str(key)+" is not present in object2"}})

print(res)
            
