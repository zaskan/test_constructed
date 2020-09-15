#!/usr/bin/python

import json

with open("origin/zaskan.json") as json_file:
  data=json.load(json_file)

print(data)
