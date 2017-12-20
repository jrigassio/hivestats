#!/bin/bash
h_string=$'Welcome to Hivestats, a tool to help you navigate the UC Berkeley EECS instructional computers. \nBuilt by James Rigassio, with inspiration taken from Allen Guo\'s Hivemind (http://aguo.us/hivemind/) \nAvailable commands / flags are:\n
-l: Optimal Login; remotely connects you to the least used server via SSH (prompts for credentials)\n
-d: Display; prints a table of all servers and usage to terminal output\n
-v: Version; gives version info\n
-h: Help; displays this menu'
if [ -z "$1" ] || [ "$1" == "-h" ]; then
  echo "$h_string"
else
  case "$1" in
    -v)
    echo "v1.0. Collaborate on this project! Github URL -> https://github.com/jrigassio/hivestats";;
    -d)
    echo "display table";;
    *)
    echo "Invalid argument: ${1}"
  esac
fi
