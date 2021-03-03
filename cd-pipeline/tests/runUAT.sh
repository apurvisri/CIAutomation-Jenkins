#!/bin/bash

#This script runs the UAT test or end to end test

#set Variable 
hostname='localhost'
port=$1

#wait for the app to start
sleep 5

#ping the app
status_code=$(curl --write-out %{http_code} --out /dev/null --silent ${hostname}:${port})


if [$http_code == 200 ];
then 
    echo "PASS: ${hostname}:${port} is reachable"
else
    echo "FAIL: ${hostname}:${port} is unreachable"
    exit 1 

fi
