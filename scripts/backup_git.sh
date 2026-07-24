#!/bin/bash

PROJETO="/opt/HBV-DADOS"

cd $PROJETO || exit 1

git add .

if git diff --cached --quiet; then
    exit 0
fi

DATA=$(date +"%Y-%m-%d %H:%M:%S")

git commit -m "Backup automatico $DATA"

git push origin main
