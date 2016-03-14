#Import begin
import time
#Flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
#Pi camera
import picamera
#Import end

#Init camera
camera = picamera.PiCamera()
time.sleep(2)

#Create Flask app
app = Flask(__name__)

@app.route('/image/display', methods=['GET'])
def displayImage():
    #Render image layout
    return render_template('image.html')

@app.route('/image/capture',  methods=['GET'])
def captureImage():
    #Capture image from camera
    img_path = 'static/capture.jpg'
    camera.capture(img_path)

    #Return path for capture
    return jsonify(result = img_path)

if __name__ == '__main__':
    app.secret_key = 'password'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
