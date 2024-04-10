#!/bin/sh

set -ex

python app/app_backend.py >> log.txt 2>&1 &
python app/app_frontend.py