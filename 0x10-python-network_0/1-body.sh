#!/bin/bash
# Display body only if 200 the response status
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -s "$1"
