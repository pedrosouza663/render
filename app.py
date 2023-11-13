from flask import Flask
app = Flask(_name_)

@app.router('/')
def hello_world():
  return 'Hello, World'
