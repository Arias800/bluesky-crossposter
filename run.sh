#!/bin/bash

# Run once per hour if nothing else has been specified in environment variables
while :; do
  python3 crosspost.py
  sleep ${RUN_INTERVAL:-3600}
done
