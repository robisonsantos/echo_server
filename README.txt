This is a simple echo server / echo client sample code.
The sample is composed by a server, writen in python and
two possible clients: one in python using simple socket 
communication and another using html5 and websockets.

In order to run the html5 client, you need to install 
kaazing Gateway and create a route to match the server
address. This is necessary because a websocket cannot 
connect to a tcp socket directly.

To do so, follow the steps:

* go to developer.kaazing.com/downloads/
  and download the 'custom protocol' version. 

* find the file 'gateway-config-minimal.xml' and
  add the following lines to it, in the right place.

  <service>
    <accept>ws://localhost:8888/echo</accept>
    <connect>tcp://localhost:8880</connect>
    <type>proxy</type>
    <cross-site-constraint>
      <allow-origin>*</allow-origin>
    </cross-site-constraint>
  </service>


The echo server will return to the client every message it receives,
until it receives the message 'bye'. In this case, the server sends 'bye' 
back and then dies.


To run the server, execute python echo_server.py
To run the client (python), execute python client.py
To run the client (html5), open the file client.html in a browser and click the link.

Both server and client code were written using python 2.7.

Make sure to have your server running before the clients.

