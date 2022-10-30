import time

from numpy import True_

class Camera:
  @classmethod
  def Create(cls, use_pi_cam):
    if use_pi_cam:
      import picamera
      class PiCamera(Camera):
        def capture(self, img_path, res_w, res_h):
            with picamera.PiCamera() as camera:
              time.sleep(2)
              camera.resolution = (res_w, res_h)
              camera.capture(img_path)
            return True
      return PiCamera()
    else:
      import cv2
      class CvCamera(Camera):
        def __init__(self):
          self.cam = cv2.VideoCapture(0)

        def __del__(self):
          self.cam.release()

        def capture(self, img_path, res_w, res_h):
            # Update camera resolution
            self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, res_w)
            self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, res_h)

            ret, frame = self.cam.read()
            if not ret: return False
            cv2.imwrite(img_path, frame)
            return True
        
        def isReady(self):
          return self.cam.isOpened()

      return CvCamera()

  def capture(self, img_path, res_w, res_h) -> bool:
    """Retrieve an image from the camera"""
    pass

  def isReady(self) -> bool:
    """Returns true if camera is ready"""
    return True
