import picamera
from time import sleep

class ReptilesCamera():
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.__camera_setting()

    def capture(self):
        self.camera.capture('image.jpg')

    def recoding(self):
        self.camera.start_recording('video.h264')
        sleep(5)
        self.camera.stop_recording()

    def __camera_setting(self):
        self.camera.sharpness = 0
        self.camera.contrast = 0
        self.camera.brightness = 50
        self.camera.saturation = 0
        self.camera.ISO = 0
        self.camera.video_stabilization = False
        self.camera.exposure_compensation = 0
        self.camera.exposure_mode = 'auto'
        self.camera.meter_mode = 'average'
        self.camera.awb_mode = 'auto'
        self.camera.image_effect = 'none'
        self.camera.color_effects = None
        self.camera.rotation = 0
        self.camera.hflip = False
        self.camera.vflip = False
        self.camera.crop = (0.0, 0.0, 1.0, 1.0)

