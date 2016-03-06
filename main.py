#Import begin
#Flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
#Import end

#Create Flask app
app = Flask(__name__)

@app.route('/image')
def displayImage():
    return render_template('image.html')

if __name__ == '__main__':
    app.secret_key = 'password'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
