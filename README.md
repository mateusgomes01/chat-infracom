# chat-infracom
Infracom chat project using [python's socket library](https://docs.python.org/3/library/socket.html)

## Usage

This first version works by first running `python UDPServer.py` then running `python UDPClient.py`. The server code will create a server instance which receives messages in lowercase and returns them in uppercase. The client code will estabilish a connection via a socket to the server, ask you for a message in lowercase and after that it'll receive the same message but in uppercase letters. The files are already configured to use the **__localhost__** as the hostname so you can run it on your own machine to test it out.
