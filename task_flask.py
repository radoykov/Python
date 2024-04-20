from flask import flask
from flask import jsonify

def fact(var):
    if var == 0:
        return 1
    else:
        return var * fact(var - 1)
    
@app.route('factoriel/', method = [GET])
def get_fact():
    num =int(request.args.get('num'))
    result = fact(num)
    return jsonify({'result':result})

if __name__ == '__main__':
    app.run(debug = True.)
    