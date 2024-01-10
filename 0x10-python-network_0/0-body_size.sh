#!/bin/bash
# takes in an url and send a requests to that url
curl -sI $1 | grep Content-Length | cut -d ' ' -f2
