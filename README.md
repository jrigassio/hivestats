# hivestats
A command line interface that monitors CPU usage data for instructional accounts in the EECS department at UC Berkeley.

Hivestats is a tool that helps Berkeley students SSH into an instructional account that will offer them the best performance.
You can monitor CPU usage [on Allan Guo's site](http://aguo.us/hivemind/) and pick a low-use machine on your own, but with this command-line utility, that is done for you. A simple command, `hivestats login` gets you to the best-available EECS instructional account.

## Installation 
### Installing hivestats
1. Download the latest release
2. Unzip the compressed directory, and navigate to it in your shell
3. Run the install script:

`sudo bash install.sh`

### Uninstalling hivestats
1. Navigate to the unzipped directory
2. Run the uninstall script:

`sudo bash uninstall.sh`

These scripts require super-user priviledges (`sudo`) to do the following:

Install
- make a directory in /usr/local/bin/
- copy files to /usr/local/bin/

Uninstall
- remove a directory from /usr/local/bin/
- remove files from /usr/local/bin/

If you'd rather not run these scripts as sudo, simply move the files yourself.
