#!/usr/bin/python

import json

with open("zaskan.json") as json_file:
  data=json.load(json_file)

print(data)
