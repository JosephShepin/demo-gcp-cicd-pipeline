from flask import Flask,Response,jsonify, render_template ,logging,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
