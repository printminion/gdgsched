#!/bin/bash

echo Start local server
dev_appserver.py --address=0.0.0.0 --port=8082 ./src/

