import socket
from flask import Flask, request, render_template

import sys
import os
import optparse
import time
import platform

app = Flask(__name__)

start = int(round(time.time()))

@app.route("/")
def index():

    return render_template('index.html', 
      name = os.environ['NAME'],
      host = socket.gethostname(),
      ipaddress = socket.gethostbyname(socket.gethostname()), 
      remote=request.remote_addr,
      architecture=platform.architecture()[0],
      machine=platform.machine(),
      node=platform.node(),
      system=platform.system()
)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(80), debug=False)