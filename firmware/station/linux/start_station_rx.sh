#!/bin/sh
# Start station_rx.py at boot (user crontab: @reboot, no sudo needed).
# Waits for arduino-router's socket, then logs CSV and the latest reading
# that the dashboard reads. Install on the board:
#   (crontab -l 2>/dev/null; echo "@reboot $HOME/station/start_station_rx.sh") | crontab -
for _ in $(seq 1 90); do
	[ -S /var/run/arduino-router.sock ] && break
	sleep 2
done
cd "$(dirname "$0")" || exit 1
exec python3 -u station_rx.py --csv station.csv --latest latest.json >>station_rx.log 2>&1
