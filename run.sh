#!/usr/bin/env bash

spurs_interval_seconds=${SPURS_INTERVAL_SECONDS:=30}
spurs_target=${SPURS_TARGET:=127.0.0.1}

source .venv/bin/activate

echo "Starting Spurs checking $spurs_target every $spurs_interval_seconds seconds"
while true; do
  python3 main.py
  sleep "$spurs_interval_seconds"
done
