# Parameters
## PID
P = 8, I = 14, D = 0.55

# Working with Github

## To run the code
sudo python3 /home/pi/Desktop/Brain-master/main.py

## For Windows

1) Install GitHub Desktop
2) In File / Clone repository
3) Paste updated files in cloned repository
4) Put commit message (Summary of changes) and press the Commit button
If you want to update your project with Github, press the Fetch origin button

## For BFMC Car - Raspberry
// For installing
git clone https://github.com/seifelius/Brain-master.git

// To make changes to Github

0) Look the password and commands in file on desktop
1) cd /home/pi/Desktop/Brain-master
2) git add .
3) git commit -m "Write changes"
4) git push

// To update from Github

0) Look the password and commands in file on desktop
1) cd /home/pi/Desktop/Brain-master
2) git pull




## Terminal output
Starting the processes! [<CameraProcess(CameraProcess-1, initial daemon)>, <CameraStreamerProcess(CameraStreamerProcess-2, initial daemon)>, <SerialHandlerProcess(SerialHandlerProcess-3, initial daemon)>, <RemoteControlReceiverProcess(RemoteControlReceiverProcess-4, initial daemon)>]
/usr/lib/python3/dist-packages/picamera/encoders.py:521: PiCameraAlphaStripping: using alpha-stripping to convert to non-alpha format; you may find the equivalent alpha format faster
  "using alpha-stripping to convert to non-alpha "
Process CameraStreamerProcess-2:
Traceback (most recent call last):
  File "/usr/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
    self.run()
  File "/home/pi/Desktop/Brain-master/src/utils/camerastreamer/CameraStreamerProcess.py", line 61, in run
    self._init_socket()
  File "/home/pi/Desktop/Brain-master/src/utils/camerastreamer/CameraStreamerProcess.py", line 87, in _init_socket
    self.client_socket.connect((self.serverIp, self.port))
OSError: [Errno 113] No route to host


