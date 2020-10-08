"""
Python Flask application to report system metrics via a public api.

The primary purpose is to report the CPU temperature for my Raspberry Pi
Cluster project. See
https://agarthetiger.github.io/mkdocs/raspberry-pi/raspberry-pi-cluster/part-1/
"""

import re
import subprocess
from flask import Flask, jsonify


app = Flask(__name__)
re_temp = re.compile(r"(?P<temp_value>\d+\.\d)(?:')(?P<temp_units>\w)", re.MULTILINE)


@app.route('/')
def root_api():
    global re_temp
    process = subprocess.run(['vcgencmd', 'measure_temp'],
                             stdout=subprocess.PIPE,
                             universal_newlines=True)
    # Assuming vcgencmd measure_temp continues to output like "temp=47.0'C\n"
    # group(0) will contain the whole match (including non-capturing groups)
    # group(1) will contain the decimal temperature value
    # group(2) will contain the temperature units
    return re_temp.search(process.stdout).group('temp_value')

@app.route('/temp')
def temp_api():
    global re_temp

    process = subprocess.run(['vcgencmd', 'measure_temp'],
                             stdout=subprocess.PIPE,
                             universal_newlines=True)

    temp_value = re_temp.search(process.stdout).group('temp_value')
    temp_units = re_temp.search(process.stdout).group('temp_units')

    data = {
        "temp": temp_value,
        "units": temp_units
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
