# chat-infracom
Infracom chat project using [python's socket library](https://docs.python.org/3/library/socket.html)

[Link](https://github.com/mateusgomes01/chat-infracom) to the project repo

## Usage
This first version works by first running `python UDPServer.py` then running `python UDPClient.py <file_to_be_Sent>`. The server will receive the file sent by the client and will also send the the file back to the client renamed. Everything is set up to use the **__localhost__** as the hostname so you can run it on your own machine to test it out.