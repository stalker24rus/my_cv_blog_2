HI ALL!
---

It is the project of the my site with blog. You can use the source code if you want for yours. But please do not use information from my cv, and rename blog page =).


# How to deploy project on server

#1. Security setups
1.1. Add new sudo user
> $ useradd nonroot
> $ passwd nonroot
> New password: 
> Retype new password: 
> passwd: password updated successfully

1.2. Add user to sudorer user group
> serv:~# usermod -aG sudo stalker

1.3. Check privileges
> $ su - stalker
> $ sudo ls -l /root
> total 0

1.4. Add home directory with .ssh dir and authorized_keys file for nonroot user
> $ sudo mkhomedir_helper nonroot && mkdir ~/.ssh && touch authorized_keys && vi authorized_keys
Enter the SSH public key, check connection from other the Terminal, and then do next steps.

1.5.Change settings in sshd config file
> $vi /etc/ssh/sshd_config

Search and change:
PasswordAuthentication no
PermitRootLogin no
Port 55555

Number of port maybe any.

1.6 Restart sshd
> $ sudo service sshd restart


2. Install general pakages

> $ sudo apt-get update && sudo apt-get install -y vim zsh tmux htop git curl wget unzip zip gcc build-essential make w3m

Change shell to zsh:
> $chsh -s $(which zsh)
Type zsh
> zsh

3. Install Git
By default the linux distr need have Git, if not then command:
> $ sudo apt install git
 
4. Install Docker
Prepere, install some the packages
> $ sudo apt install apt-transport-https ca-certificates software-properties-common
> $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
> $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
> $ sudo apt update

Check place for download the docker package
> $ apt-cache policy docker-ce

Install docker
> $ sudo apt install docker-ce

Check status
> $ sudo systemctl status docker

Add current user to docker group
> $ sudo usermod -aG docker ${USER}


5. Install Docker-compose
Check last version on https://github.com/docker/compose/releases

Get and install:
> $ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

Do executable:
> sudo chmod +x /usr/local/bin/docker-compose

Check:
> $ docker-compose --version

6. Install Docker Compose


7. Download project



8. Prepare system dirs for working with a Docker volumes



