import sys
import json

def f(test):
    test['value'] = values.get(test['id'], '')
    if 'values' in test:
        for i in test['values']:
            f(i)

values = json.load(open(sys.argv[1]))
values = {value['id'] : value['value'] for value in values['values']}

tests = json.load(open(sys.argv[2]))

for i in tests['tests']:
    f(i)

json.dump(tests, open(sys.argv[3], 'w'), indent=2)