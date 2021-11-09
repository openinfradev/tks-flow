#!/usr/bin/python3
def terraform_style_print(arr, sep):
  refined=[]
  for i in arr:
    refined.append('{0}{1}{0}'.format(sep, i.replace('"','').replace("'",'')))

  print('[{}]'.format(",".join(refined)))

def list_print(arr, sep):
  refined=[]
  for i in arr:
    refined.append('{0}{1}{0}'.format(sep, i.replace('"','').replace("'",'')))

  print(" ".join(refined))
