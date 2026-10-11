#!/bin/sh
# Render the video cards to 1920x1080 PNG. Run from the repository root after
# `uv run python -m poopvolt.report`. rsvg-convert only loads images next to the
# card, so the generated chart is copied into cards/ first.
set -eu
cp docs/images/comparison-inverter-1-replayed.svg docs/video/cards/chart-inverter-1.svg
docker run --rm -v "$PWD/docs/video/cards":/cards -w /cards alpine:3.20 sh -c '
  apk add -q --no-cache rsvg-convert font-dejavu >/dev/null
  for f in 0*.svg; do rsvg-convert -w 1920 -h 1080 "$f" -o "${f%.svg}.png"; done
  chown '"$(id -u):$(id -g)"' ./*.png'
