from flask import Flask, jsonify
import subprocess

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    cmd = "ls -l"
    res = subprocess.call(cmd.split())
    print(res)
    return jsonify({
        "result": "command sent!!"
    })


if __name__ == '__main__':
    app.run()
