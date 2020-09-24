from flask import Flask
app = Flask(__name__)

import time 

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
     localtime = time.asctime( time.localtime(time.time()) )
     return localtime

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
