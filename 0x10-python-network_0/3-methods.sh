#!/bin/bash
curl -sI "$1" | awk '/Allow/ {print $2}' | cut -d " " -f 2-
