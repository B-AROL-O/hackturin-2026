#!/bin/sh
set -eu
node scripts/music.mjs
ffmpeg -y -hide_banner -loglevel error -i audio/narration-raw.wav -af loudnorm=I=-16:TP=-1.5:LRA=7 -ar 48000 audio/voice-master.wav
ffmpeg -y -hide_banner -loglevel error -i audio/voice-master.wav -i audio/music.wav -filter_complex '[0:a][1:a]amix=inputs=2:normalize=0,alimiter=limit=0.891:level=false,afade=t=out:st=117:d=2' -ar 48000 -c:a pcm_s24le audio/narration.wav
