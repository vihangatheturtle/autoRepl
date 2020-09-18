# autoRepl - a powerful stress testing tool
autoRepl uses [repl.it](https://repl.it) to create a powerful stress testing without affecting the internal network

# How to use
 - Fork this repo
 - Replace the example url with your github fork link in the 'start.bat' file.
 - Replace 0.0.0.0 (IPADDR) and 80 (PORTNUM) with the target IP address and port in 'main.py'
 - Make sure all prerequisites from 'requirments.txt' are installed (pip)
 - run 'start.bat' or manually run 'main.py'

#How does it work
autoRepl uses [repl.it](https://repl.it) to create an unlimited number of bots which can all flood an IP address through a udp request. It can automatically create a repl from your github fork of this repo and start flooding.
