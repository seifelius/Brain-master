# Copyright (c) 2019, Bosch Engineering Center Cluj and BFMC organizers
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE

import json
import socket
import time

from threading       import Thread

from src.templates.workerprocess import WorkerProcess

import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(-1)

def points_in_row_by_midle(row_to, sector_start, sector_end):
    ret, image = cap.read()
    image_width = image.shape[1]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_gray = cv2.GaussianBlur(gray,(5, 5), 0)
    edges = cv2.Canny(blur_gray, 50, 150)
    #cv2.imshow('frame', image)

    #search_middle = int((sector_start + sector_end) / 2)
    search_middle = int((sector_start + image_width) / 2)
    edges_x = []
    midle_x = 0
    for i in range(search_middle - 1):
        if edges[row_to][search_middle + i] != 0:
            edges_x.append(search_middle + i)
            break
    for i in range(search_middle - 1):
        if edges[row_to][search_middle - i] != 0:
            edges_x.append(search_middle - i)
            break
    
    if len(edges_x) < 2: return 'Less than 2 edges', midle_x, edges_x, 0, image_width
    else:
        edges_x.sort()
        midle_x = int((edges_x[-1] + edges_x[0]) / 2)
        lenght_of_road = int((edges_x[-1] - edges_x[0])/2)
        return 'None', midle_x, edges_x, lenght_of_road, image_width



class RemoteControlReceiverProcess(WorkerProcess):
    # ===================================== INIT =========================================
    def __init__(self, inPs, outPs):
        """Run on raspberry. It forwards the control messages received from socket to the serial handler
        
        Parameters
        ------------
        inPs : list(Pipe)
            List of input pipes (not used at the moment)
        outPs : list(Pipe) 
            List of output pipes (order does not matter)
        """

        super(RemoteControlReceiverProcess,self).__init__( inPs, outPs)

    # ===================================== RUN ==========================================
    def run(self):
        """Apply the initializing methods and start the threads
        """
        self._init_socket()
        super(RemoteControlReceiverProcess,self).run()

    # ===================================== INIT SOCKET ==================================
    def _init_socket(self):
        """Initialize the communication socket server.
        """
        # self.port       =   12244
        # self.serverIp   =   '0.0.0.0'

        # self.server_socket = socket.socket(
        #                             family  = socket.AF_INET, 
        #                             type    = socket.SOCK_DGRAM
        #                         )
        # self.server_socket.bind((self.serverIp, self.port))
        
        
        
        # self.server_socket.close()

    # ===================================== INIT THREADS =================================
    def _init_threads(self):
        """Initialize the read thread to transmite the received messages to other processes. 
        """
        readTh = Thread(name='ReceiverCommandThread',target = self._read_stream, args = (self.outPs, ))
        self.threads.append(readTh)

    # ===================================== READ STREAM ==================================
    def _read_stream(self, outPs):
        """Receive the message and forwards them to the SerialHandlerProcess. 
        
        Parameters
        ----------
        outPs : list(Pipe)
            List of the output pipes.
        """
        
        try:
            while True:
                
                Status, midle, edges_x, lenght, image_widt = points_in_row_by_midle(50, 0, 520)
                Status2, midle2, edges_x2, lenght2, image_widt2 = points_in_row_by_midle(50, 0, 520)
                
                #print(image_widt)
                
                command = ''
                # left or right
                if int(image_widt / 2 - 50) < midle: command = 'TurnRight'
                elif int(image_widt / 2 + 50) < midle: command = 'TurnLeft'
                else: command = 'Straight'
                
                '''
                command_list = ['Forward', 'TurnRight', 'TurnLeft', 'Straight', 'Stop']
                
                

                for command in command_list:

                    if command == 'Forward':
                        write = {'action': '1', 'speed': 0.20} #command for riding forward (backward with minus, ex. -0.2)
                    elif command == 'Stop':
                        write = {'action': '1', 'speed': 0.0} #stop

                    if command == 'TurnRight':
                        write = {'action': '2', 'steerAngle': 14.0} #command for turning steers Right
                    elif command == 'TurnLeft':
                        write = {'action': '2', 'steerAngle': -14.0} #command for turning steers Left
                    elif command == 'Straight':
                        write = {'action': '2', 'steerAngle': 0.0} #command for turning steers straight

                    for outP in outPs:
                        outP.send(write)
                        outP.send(write)
                        outP.send(write)
                        print(command)
                    
                    time.sleep(0.2)
                '''
                if command == 'Forward':
                    write = {'action': '1', 'speed': 0.20} #command for riding forward (backward with minus, ex. -0.2)
                elif command == 'Stop':
                    write = {'action': '1', 'speed': 0.0} #stop

                if command == 'TurnRight':
                    write = {'action': '2', 'steerAngle': 14.0} #command for turning steers Right
                elif command == 'TurnLeft':
                    write = {'action': '2', 'steerAngle': -14.0} #command for turning steers Left
                elif command == 'Straight':
                    write = {'action': '2', 'steerAngle': 0.0} #command for turning steers straight

                for outP in outPs:
                    outP.send(write)
                    outP.send(write)
                    outP.send(write)
                    print(command)
                    
                time.sleep(0.2)
                
        except Exception as e:
            print(e)
