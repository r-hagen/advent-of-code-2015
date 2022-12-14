import json
input = json.loads(open('d12.in').read().strip())

def traverse(n, sum=0):
    if isinstance(n, int):
        sum += n
    elif isinstance(n, list):
        for c in n:
            sum += traverse(c)
    elif isinstance(n, dict):
        if 'red' in n.keys() or 'red' in n.values():
            pass
        else:
            for k, v in n.items():
                sum += traverse(v)
    return sum
    
assert(traverse(json.loads('[1,2,3]'))) == 6
assert(traverse(json.loads('[1,{"c":"red","b":2},3]'))) == 4
assert(traverse(json.loads('{"d":"red","e":[1,2,3,4],"f":5}'))) == 0
assert(traverse(json.loads('[1,"red",5]'))) == 6

print(traverse(input))
