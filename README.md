# FLiR_Stream_Over_Websocket_HTTP_Server

This project is an enhanced version of the websocket_http_server that I wrote that is designed to be used specifically with the FLiR Lepton Camera.

Websocket_HTTP_Server is a collection of files that will easily display a set of data being gathered over a web browser, the collection was originally built to display thermal images over http/tcp port 80 in a real-time fasion. When connecting to the http server, the server delieves index.html that will launch a javascript program on load. This program connects to the websocket server, where the websocket server pushes data down to all the clients.

By running websocket_http_server.py, the python program will startup an http server and a websocket server which will pull configuration settings from server.conf which also has a file path to the image that will be constantly sent in a loop. The program will encode thermal.jpg into a base64 format and sent it over the websocket connection.

Furthermore, I added FLiR Lepton cammera support to the websocket_http_server.py, in which the program will save the file as a jpeg in the form of a matplot heatmap.

server.conf is the configuration file that websocket_http_server.py will use in order to determine that port and interface numbers that the servers will broadcast on.

index.html is server by the http server, which onload will hook into the websocket server. index.html will collect the data that is being streamed from the websocket server and display it as an image by decoding the image and placing it on the web browser. index.html handles the formating of the image in terms of the dimensions that it will be displayed as.
