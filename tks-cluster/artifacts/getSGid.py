#!/usr/local/bin/python3
import yaml, os, sys
from common import *

def get_sgs(stream):
  sgs=[]
  try:
    parsed = yaml.safe_load(stream)
    for entry in parsed['status']['outputs']:
      if entry['key']=="id":
        sgs.append(entry['value'])
  except yaml.YAMLError as exc:
    print(exc)
  except TypeError as exc:
    print(exc)
  return sgs

stream = os.popen('kubectl get workspaces -n {} taco-security-group -o yaml'.format(sys.argv[1]))
sgs=get_sgs(stream)
terraform_style_print(sgs,'"')