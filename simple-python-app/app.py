from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! I'm Aditya Kumar this is a CI/CD pipeline project'

if __name__ == '__main__':
    app.run()

