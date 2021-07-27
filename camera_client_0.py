import imagezmq
from imutils.video import VideoStream

path = "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov"  # change to your IP stream address
cap = VideoStream(path)

sender = imagezmq.ImageSender(connect_to='tcp://localhost:5555')  # change to IP address and port of server thread
cam_id = 'Camera 1'  # this name will be displayed on the corresponding camera stream

stream = cap.start()

while True:
    frame = stream.read()
    sender.send_image(cam_id, frame)
