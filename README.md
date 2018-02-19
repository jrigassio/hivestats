# hivestats
A command line interface that monitors CPU usage data for instructional accounts in the EECS department at UC Berkeley.

Hivestats is a tool that helps Berkeley students SSH into an instructional account that will offer them the best performance.
You can monitor CPU usage [on Allan Guo's site](http://aguo.us/hivemind/) and pick a low-use machine on your own, but with this command-line utility, that is done for you. A simple command, `hivestats login` gets you to the best-available EECS instructional account.

## Installation (for Mac OSX, Linux, and other UNIX-like systems)
### Installing hivestats
1. Download the latest release
2. Unzip the compressed directory, and navigate to it in your shell
3. Run the install script:

`./install.sh`
* Depending on your environment, you may need to escalate to super-user privileges (`sudo bash install.sh`) 

### Uninstalling hivestats
1. Navigate to the unzipped directory
2. Run the uninstall script:

`./uninstall.sh`
* Depending on your environment, you may need to escalate to super-user privileges (`sudo bash uninstall.sh`)

## hivestats for Windows
There is currently no stable release for Windows. I would recommend that Windows users look into the [Linux Subsystem for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10), as having a UNIX-like command line interface will let you use hivestats. Feel free to [open an issue](https://help.github.com/articles/creating-an-issue/) if you're interested in building a full-fledged Windows compatible version.
