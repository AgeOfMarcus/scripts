#!/bin/bash
echo "Restarting services..."
service NetworkManager restart
service network-manager restart
service wpa_supplicant restart
service dhclient restart
echo "Re-enabling wlan0"
ifconfig wlan0 down
ifconfig wlan0 up
echo "Scanning for access points..."
scan-wifi
echo "Fixed! The panel will still not work, though."
echo "If it's still not working, try cleaning NetworkManager.conf:"
echo "nano /etc/NetworkManager/NetworkManager.conf"
