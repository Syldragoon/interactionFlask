#Import begin
#Flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
#Camera
from camera import Camera
#Import end

# Use Pi camera or not
use_pi_cam = False

#Utility methods begin
def isAsInt(iStr):
    '''Check whether or not a string can be casted to an int'''
    asInt = False
    try:
        int(iStr)
        asInt = True
    except ValueError:
        pass
    return asInt
#Utility methods end

#Create Flask app
app = Flask(__name__)

#Init camera
cam = Camera.Create(use_pi_cam)

#Make sure camera is ready
if not cam.isReady():
  print('Camera is not ready!')
  exit(-1)

@app.route('/image/display', methods=['GET'])
def displayImage():
    #Render image layout
    return render_template('image.html')

@app.route('/image/capture',  methods=['GET'])
def captureImage():
    #Capture image from camera
    #Variables
    img_path = 'static/capture.jpg'

    #Default resolution
    res_w = 640
    res_h = 480

    #Retrieve resolution if possible
    resolution = request.args.get('resolution', '', type=str)
    widthHeight = resolution.split('x')
    if len(widthHeight) == 2 and isAsInt(widthHeight[0]) and isAsInt(widthHeight[1]):
        res_w = int(widthHeight[0])
        res_h = int(widthHeight[1])
        print('Resolution retrieved: %dx%d' % (res_w, res_h))

    #Capture from camera
    if not cam.capture(img_path, res_w, res_h):
      img_path = ''

    #Return path for capture
    return jsonify(result = img_path)

if __name__ == '__main__':
    app.secret_key = 'password'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=False)
