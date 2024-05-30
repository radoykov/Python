from flask import Flask, request, jsonify, app
import time

app = Flask(__name__)  

initial_time = time.gmtime(0)

@app.route('/timer', methods = ['POST'])

def post_mes():
    global initial_time 
    initial_time = time.time()
    return jsonify({'message':'Timer started.'})

@app.route('/timer', methods = ['GET'])

def get_time():
    global initial_time
    result = 0
    if initial_time != time.gmtime(0):
        result = time.time() - initial_time
    return jsonify({'Time passed:': time.strftime("%H:%M:%S", time.gmtime(result))})
    
    
@app.route('/timer', methods = ['DELETE'])

def reset_timer():
    global initial_time
    initial_time = time.gmtime(0)
    return jsonify({'message':'Timer stopped.'})
    



if __name__ == '__main__':
    app.run(debug=True)