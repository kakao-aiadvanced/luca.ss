#!/bin/bash

# ollama start
# ollama run phi3
# ollama run llama3

curl -XPOST http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt":"Why is the sky blue?",
  "stream": false
}'