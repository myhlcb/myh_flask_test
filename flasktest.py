# from flask import Flask
from flask import Flask
from package_myh.test1 import test1_print
test1_print()
app = Flask(__name__)
@app.route('/hello')

def hello_wordle():
    return 'Hello World!'
if __name__=='__main__':
    app.run(host='localhost', port=5000)