from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/patpat')
def pat_pat():
    mul = multiply(5, 6)
    return 'I love %d dinosaurs!!!\n' % mul

def multiply(a, b):
    return a * b

@app.route('/args', methods=['POST'])
def args_fun():
    args = request.form
    print(args)
    arg1 = args.get('arg1')
    arg2 = args.get('arg2')
    return 'I love dinosaurs!!! Especially %s and %s \n' % (arg1, arg2)

def multiply(a, b):
    return a * b

if __name__ == '__main__':
    app.run(port=5001)
