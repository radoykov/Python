from flask import Flask, request, jsonify, app

app = Flask(__name__)

def fact(var):
    if var == 0:
        return 1
    else:
        return var * fact(var - 1)
    
@app.route('/factorial', methods = ['GET'])

def get_fact():
    num =int(request.args.get('num'))
    result = fact(num)
    return jsonify({'result':result})

if __name__ == '__main__':
    app.run(debug=True)
