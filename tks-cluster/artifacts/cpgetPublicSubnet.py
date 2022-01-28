#!/usr/local/bin/python3
import yaml, os, sys
from common import *

def get_subnets(stream):
  subnets=[]
  try:
    parsed = yaml.safe_load(stream)
    for entry in parsed['spec']['network']['subnets']:
      if entry['isPublic']:
        subnets.append(entry['id'])
  except yaml.YAMLError as exc:
    print(exc)
  except TypeError as exc:
    print(exc)
  return subnets

stream = os.popen('kubectl get awscluster -n argo {} -o yaml'.format(sys.argv[1]))
subnets=get_subnets(stream)
list_print(subnets,' ')
