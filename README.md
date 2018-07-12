# FLiR_Stream_Over_Websocket_HTTP_Server

This project is an enhanced version of the websocket_http_server that I wrote, which is designed to be used specifically with the FLiR Lepton Camera to stream data to a browser over a websocket connection after being served index.html through http, in which index.html launches a small javascript program to hook into the websocket server to collect image data.

![alt+text](https://raw.githubusercontent.com/cj667113/FLiR_Stream_Over_Websocket_HTTP_Server/master/Img/Capture.JPG)

Please setup the FLiR camera to the microcontroller properly. For a Raspberry Pi 3, it will look like:
![alt+text](https://raw.githubusercontent.com/cj667113/FLiR_Stream_Over_Websocket_HTTP_Server/master/Img/HW_Set_2.jpg) ![alt+text](https://raw.githubusercontent.com/cj667113/FLiR_Stream_Over_Websocket_HTTP_Server/master/Img/HW_Set_1.jpg)

Furthermore, since we planned on deploying the FLiR Lepton further away from where the Raspberry Pi 3 will be located, we decided that it would be best to connect the connector pins to a female RJ45 Connector, both for the camera and the Raspberry Pi 3. This way, we could use an ethernet cord to act as an extension cord from the Raspberry Pi 3 to the Camera.

<p><img src="https://github.com/cj667113/FLiR_Stream_Over_Websocket_HTTP_Server/blob/master/Img/RJ45_5.jpeg" height="20%" width="20%"/><img src="https://github.com/cj667113/FLiR_Stream_Over_Websocket_HTTP_Server/blob/master/Img/RJ45_3.jpg" height="20%" width="20%"/></p>
<img src="https://github.com/cj667113/FLiR_Stream_Over_Websocket_HTTP_Server/blob/master/Img/RJ45_2.jpg" height="20% width="20%"/>
<img src="https://github.com/cj667113/FLiR_Stream_Over_Websocket_HTTP_Server/blob/master/Img/RJ45_1.jpg" height="20% width="20" />
<img src="https://raw.githubusercontent.com/cj667113/FLiR_Stream_Over_Websocket_HTTP_Server/master/Img/RJ45_4.jpg" height="20% width=20%/>

Websocket_HTTP_Server is a collection of files that will easily display a set of data being gathered over a web browser, the collection was originally built to display thermal images over http/tcp port 80 in a real-time fashion. When connecting to the http server, the server delivers index.html to the client that will launch a javascript program on load. This program connects to the websocket server, where the websocket server will stream to all the clients.

By running websocket_http_server.py, the python program will startup an http server and a websocket server which will pull configuration settings from server.conf which also has a file path to the image that will be constantly sent in a loop. The program will encode thermal.jpg into a base64 format and sent it over the websocket connection.

[Click here for more information about the websocket_http_server.py](https://github.com/cj667113/Websocket_HTTP_Server "cj667113/Websocket_HTTP_Server ")

In order to get this to work, you will need to import these packages:

![alt+text](https://raw.githubusercontent.com/cj667113/FLiR_Stream_Over_Websocket_HTTP_Server/master/Img/packages_needed.jpg)

Furthermore, I added FLiR Lepton cammera support to the websocket_http_server.py, in which the program will save the file as a jpeg in the form of a matplot heatmap.

![alt+text](https://raw.githubusercontent.com/cj667113/FLiR_Stream_Over_Websocket_HTTP_Server/master/Img/FLiR_program_module.jpg)

server.conf is the configuration file that websocket_http_server.py will use in order to determine that port and interface numbers that the servers will broadcast on, as well as the image data that will be sent over the websocket connection.

![alt+text](https://raw.githubusercontent.com/cj667113/FLiR_Stream_Over_Websocket_HTTP_Server/master/Img/server_conf.jpg)

index.html is server by the http server, which onload will hook into the websocket server. index.html will collect the data that is being streamed from the websocket server and display it as an image by decoding the image and placing it on the web browser. index.html handles the formating of the image in terms of the dimensions that it will be displayed as.

![alt+text](https://raw.githubusercontent.com/cj667113/FLiR_Stream_Over_Websocket_HTTP_Server/master/Img/index.jpg)
