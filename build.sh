#!/usr/bin/venv bash
virtualenv -p python3 venv
source venv/bin/activate
pip3 install --pre pybuilder
pyb clean
pyb -v
pip install target/dist/Bakery-1.0.dev0/dist/Bakery-1.0.dev0.tar.gz
