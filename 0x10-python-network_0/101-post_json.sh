#!/bin/bash
# Sends a JSON POST request to a given URL with a given JSON file.
cat "$2" | curl -s -H "Content-Type: application/json" -d @- "$1"
