#!/bin/bash
#display body response
curl -sI "$1" | grep 'Content-Length' | cut -d ' ' -f2
