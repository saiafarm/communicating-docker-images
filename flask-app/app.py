from flask import Flask
import requests

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello from Flask!"

@app.route('/spring-hello')
def spring_hello():
    response = requests.get('http://spring-boot-app:8080/hello')
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
