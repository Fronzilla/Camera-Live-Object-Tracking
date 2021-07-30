import imagezmq
from imutils.video import VideoStream

# path = "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov"  # change to your IP stream address
path = "rtsp://admin:091027@37.192.38.33:9784/cameras/10/streaming/main?authorization=Basic%20d2ViOg=="
cap = VideoStream(path)

sender = imagezmq.ImageSender(connect_to='tcp://localhost:5555')  # change to IP address and port of server thread
cam_id = 'Camera 1'  # this name will be displayed on the corresponding camera stream

stream = cap.start()

while True:
    frame = stream.read()
    sender.send_image(cam_id, frame)
