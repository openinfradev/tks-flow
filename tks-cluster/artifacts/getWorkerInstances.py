#!/usr/local/bin/python3
import yaml, os, sys
from common import *

def get_workers(stream):
  workers=[]
  try:
    parsed = yaml.safe_load(stream)
    for entry in parsed['status']['instances']:
      workers.append(entry['instanceID'])
  except yaml.YAMLError as exc:
    print(exc)
  except TypeError as exc:
    print(exc)
  return workers

allworker=[]
stream = os.popen('kubectl get awsmachinepool -n argo {0}-taco-mp-0 -o yaml'.format(sys.argv[1]))
allworker.extend(get_workers(stream))
terraform_style_print(allworker,'"')