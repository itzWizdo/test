from flask import Flask, request
app = Flask(__name__)
@app.route('/fetch')
def fetch():
    return {"message": "hello world"}
if __name__ == '__main__':
    app.run(debug=True, port=25565)