#!/bin/bash

if [ ! $# == 3 ]; then
  echo "Usage: vpnfix.sh /path/to/vpn.ovpn username password"
  exit
fi

file_path=$(dirname $1)
echo $file_path

echo $2 > $file_path/cred.txt
echo $3 >> $file_path/cred.txt

echo "auth-user-pass cred.txt" >> $1
openvpn $1
