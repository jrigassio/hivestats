#!/bin/sh
# Don't modify this script and expect it to work.
# Direct any and all questions to James Rigassio - jrigassio@berkeley.edu
echo ~~~ hivestats Installation Script ~~~
echo Checking for Python 3.x
if command -v python3 &>/dev/null; then
    echo Python 3 is installed. \'hivestats\' and \'usage.py\' are copied into /usr/local/bin.
    mkdir /usr/local/bin/hive-cli/
    echo "*"
    cp hivestats /usr/local/bin/
    echo "*"
    cp usage.py /usr/local/bin/hive-cli/
    echo "*"
    echo Hivestats is installed! Try the command: \'hivestats login\'
else
    echo Python 3 is not installed, install the latest version to use hivestats.
    echo Find it here: https://www.python.org/downloads/
fi
