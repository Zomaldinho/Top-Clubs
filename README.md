Top Clubs in Different Countries App

This app is created to show the top football clubs in 8 different countries around the world (England, Spain, Germany, Italy, France, Nethrlands, Brazil, Egypt)
User can add additional clubs to any of the available 8 countries but he can edit or delete only the ones he created previously
User has to have a Google account and logged-in to be able to add/edit/delete clubs
The recent 5 added clubs are shown in the home page

The code is written in Python 3 using Flask framework

Use a terminal
Access this project using a Unix-style terminal on your computer. If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the Git software. If you don't already have Git installed, download Git from git-scm.com.

Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.
Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

Download the VM configuration
https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip

Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

You have to create the database using code $ python database_setup.py then update it with the default 27 clubs using this code $ python update_db.py
Finally you have to run this code in the terminal $ python app.py and access the application through your browser using the following url http://localhost:5000/main/
