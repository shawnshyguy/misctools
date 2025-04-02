#!/bin/bash

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="ram_usage_${TIMESTAMP}.log"

while true; do
    TIME=$(date +"%H:%M:%S")
    RAM_USAGE=$(free -h | awk '/Mem:/ {print $3 "/" $2}')
    echo "$TIME | RAM $RAM_USAGE" >> "$LOG_FILE"
    echo "$TIME | RAM $RAM_USAGE"
    sleep 15
done
