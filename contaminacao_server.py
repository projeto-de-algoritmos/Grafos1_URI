from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from contaminacao import start

socketio = SocketIO()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/contaminacao')
def index():
    return render_template('index.html')

@socketio.on('start')
def handle_start(message):
    print(message)
    graph = message['graph']
    n = len(message['graph'][0])
    m = len(message['graph'])
    start(socketio, graph, n, m)

if __name__ == '__main__':
    socketio.run(app)


