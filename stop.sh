#! /bin/bash
#
# Kill all current instances of app.py on this machine
#
# Used and Edited: Project 4 stop.sh

# Grep for all running processes containing app in description
# EXCEPT the grep command itself; turn them into 'kill' commands and
# execute the commands with bash
#
ps -x | grep map_server | grep -v grep | \
    awk '{print "kill " $1}' | bash


