import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    print('here', time.time())
    return {'time': time.time()}