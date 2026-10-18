#!/bin/bash

cd "$(dirname "$0")/.." || exit 1

echo "=============================="
echo "Student Information"
echo "=============================="
echo "Name: Oybek"
echo "Surname: Yuldashov"
echo "Group: IT2-2307"
echo "Student ID: 41559"

echo "=============================="
echo "System Information"
echo "=============================="
echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -s -r)"
echo "Disk Usage:"
df -h /
echo "Memory Usage:"
free -h

if [ -f Yuldashov_Oybek_info.txt ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi
