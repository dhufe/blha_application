#!/bin/sh

set -ex

unset http_proxy
unset https_proxy

cd app
python app_frontend.py >> log.txt 2>&1 &