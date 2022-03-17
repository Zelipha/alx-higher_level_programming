#!/bin/bash
#Script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message You got me!
curl -sL -X PUT -d -H "Content-Type: text/html" 0.0.0.0:5000/catch_me
