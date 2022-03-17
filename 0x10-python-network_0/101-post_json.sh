#!/bin/bash
#Sends a JSON POST request to a URL passed and displays the body
curl -d "@$2" -H "Content-Type: application/json" -sX POST "$1"
