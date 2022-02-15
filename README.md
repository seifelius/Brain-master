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


Error:

Starting the processes! [<SerialHandlerProcess(SerialHandlerProcess-1, initial daemon)>, <RemoteControlReceiverProcess(RemoteControlReceiverProcess-2, initial daemon)>]
Process RemoteControlReceiverProcess-2:
Traceback (most recent call last):
File "/usr/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
self.run()
File "/home/pi/Desktop/Brain-master/src/utils/remotecontrol/RemoteControlReceiverProcess.py", line 55, in run
self._init_socket()
File "/home/pi/Desktop/Brain-master/src/utils/remotecontrol/RemoteControlReceiverProcess.py", line 69, in _init_socket
self.server_socket.bind((self.serverIp, self.port))
OSError: [Errno 98] Address already in use


