#!/usr/bin/python

# Minimal CGI script for Online Python Tutor (v3), tested under Python 2 and 3

# If you want to run this script, then you'll need to change the
# shebang #! line at the top of this file to point to your system's Python.
#
# Also, check CGI execute permission in your script directory.
# You might need to create an .htaccess file like the following:
#
#   Options +ExecCGI
#   AddHandler cgi-script .py


import cgi
import json
import sys
import requests
import urllib


def cgi_finalizer(input_code, output_trace):
  """Write JSON output for js/pytutor.js as a CGI result."""
  t=json.loads(output_trace)
  ret = dict(code=input_code, trace=t['trace'])
  json_output = json.dumps(ret, indent=None) # use indent=None for most compact repr

  print("Content-type: text/plain; charset=iso-8859-1\n")
  print(json_output)

raw_input_json = None
options_json = None

# If you pass in a filename as an argument, then process script from that file ...
if len(sys.argv) > 1:
  user_script = open(sys.argv[1]).read()

# Otherwise act like a CGI script with parameters:
#   user_script
#   raw_input_json
#   options_json
else:
  form = cgi.FieldStorage()
  user_script = form['user_script'].value
  # for Python 2, immediately convert to utf-8 before passing input into program
  if hasattr(user_script, 'decode'):
    user_script = user_script.decode('utf-8')
  if 'raw_input_json' in form:
    raw_input_json = form['raw_input_json'].value
  if 'options_json' in form:
    options_json = form['options_json'].value

#PROBLEME ICI A CAUSE DES # dans le code

r = requests.get("http://localhost:3000/exec_c?callback=jQuery18205694860052508335_1488455900285&user_script="+urllib.quote_plus(user_script)+"&options_json=%7B%22cumulative_mode%22%3Afalse%2C%22heap_primitives%22%3Afalse%2C%22show_only_outputs%22%3Afalse%2C%22py_crazy_mode%22%3Afalse%2C%22origin%22%3A%22opt-frontend.js%22%7D&_=1488455902311")

cgi_finalizer(user_script,r.content)
