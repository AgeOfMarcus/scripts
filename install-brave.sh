#!/bin/bash

wget -O brave.deb https://laptop-updates.brave.com/latest/dev/debian64
apt-get install -y gdebi && gdebi brave.deb
rm brave.deb
