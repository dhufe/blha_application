#!/bin/sh

set -ex

cd app
python app_backend.py >> log.txt 2>&1 &