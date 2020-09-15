#!/usr/bin/python

import json

with open('origin/zaskan.json') as f:
  data = json.load(f)

print(json.dumps(data, indent = 4, sort_keys=True))
