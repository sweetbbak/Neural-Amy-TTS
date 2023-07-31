#!/bin/bash
echo "$2" | piper-tts --model "$1" --output_raw | aplay -r 22050 -c 1 -f S16_LE -t raw
