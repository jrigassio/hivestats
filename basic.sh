#!/bin/bash

argv=($1 $2 $3)
if [ -n "${argv[0]}" ]; then
    echo ${argv[0]}
else
    echo "help"
fi
