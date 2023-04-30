#!/bin/bash

cd /TCC/TCC_COLETOR

git fetch origin
git merge origin/main


while true
do 
    python mqtt.py
    echo "******"
done