#!/bin/bash
#Script that takes in a URL, request to that URL, and displays body size
curl -sI "$1" | grep Content-Length | cut -d ' ' -f 2
