#!/usr/bin/venv bash
virtualenv venv
source venv/bin/activate
pip install pybuilder
pyb clean
pyb -v
pip install target/dist/Bakery-1.0.dev0/dist/Bakery-1.0.dev0.tar.gz