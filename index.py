from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello everyone frnd'
if __name__=='__main__':
    app.run()