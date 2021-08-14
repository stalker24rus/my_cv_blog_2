WELLCOME!
---

It is project of the my site with blog. Site Powered on Django framework.  
You need use some linux distribution kit, in my case I use remote server based on Ubuntu 20.10.  
You can use the source code if you want for free.   
But please do not use information from my cv, and rename blog page ([ Я : blognote ]) =).  
If you want only check how to work project without deploying to server, then see 6 paragraph.  

------------

#1. Security setups  
1.0. Connect to server by SSH.  
1.1. Add new sudo user   
> $ useradd nonroot   
> $ passwd nonroot  
> New password:  
> Retype new password:  
> passwd: password updated successfully  

1.2. Add user to sudorer user group
> serv:~# usermod -aG sudo nonroot

1.3. Check privileges  
> $ su - nonroot
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

------------

2. Install general pakages

2.1. Type big string from here
> $ sudo apt-get update && sudo apt-get install -y vim zsh tmux htop git curl wget unzip zip gcc build-essential make w3m

2.2. Change shell to zsh:
> $chsh -s $(which zsh)  

Type zsh and tune zsh for you  
> zsh

------------

3. Install Git
3.1. By default the linux distrs have Git, if not then do command:
> $ sudo apt install git

------------ 
4. Install Docker
4.1. Prepere, install some the packages and do settings   
> $ sudo apt install apt-transport-https ca-certificates software-properties-common  
> $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  
> $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"  
> $ sudo apt update  

4.2. Check place for download the docker package
> $ apt-cache policy docker-ce

4.3. Install docker
> $ sudo apt install docker-ce

4.4. Check status
> $ sudo systemctl status docker

4.5. Add current user to docker group
> $ sudo usermod -aG docker ${USER}

------------

5. Install Docker-compose
5.1. Check last version on https://github.com/docker/compose/releases

5.2. Get and install:
> $ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

5.3. Do executable:
> sudo chmod +x /usr/local/bin/docker-compose

5.4. Check:
> $ docker-compose --version


6. Install project from github

6.1. First create project directory and go to there:
> $ sudo mkdir -p /usr/src/apps/ && cd /usr/src/apps/

6.2. Clone project from git
> $ sudo git clone https://github.com/stalker24rus/my_cv_blog_2.git

6.3. Check project
> $ ls -l

6.4. Go to my_cv_blog_2
> $ cd my_cv_blog_2

------------

7. Prepare system for working with a Docker

7.1. Create .env file with environments setting in /usr/src/apps/my_cv_blog_2 
> $ sudo touch .env && vim .env

7.2. Add environments values in file:

> \#Databse setting  
> DB_NAME=  
> DB_USER=  
> DB_PW=  
> DB_VOLUME=/var/lib/postgresql  
>  
> \# Django project settings  
> \# For generating django secret key you can use some generator from search in google  
> \# like https://djecrety.ir/ or  
> \# https://stackoverflow.com/questions/41298963/is-there-a-function-for-generating-settings-secret-key-in-django  
> DJANGO_ENV_SECRET_KEY=   
> DJANGO_ENV_EMAIL_HOST=   
> DJANGO_ENV_EMAIL_PORT=   
> DJANGO_ENV_EMAIL_HOST_USER=   
> DJANGO_ENV_EMAIL_HOST_PASSWORD=   
> DJANGO_ENV_LOG_PATH=/var/log/django/  
>   
> \# Path with static and media source for www on host mashine  
> PROJECT_WWW_PATH=/usr/src/www/  
> DJANGO_ENV_WWW_PATH=/usr/src/www/ 
> \# Gunicorn settings
> GUNICORN_LOG_PATH= /var/log/gunicorn   
>  
> \# Nginx   
> NGINX_LOG_PATH=/var/log/nginx  
> \# If used sertificate if do not then need change file nginx/nginx.conf  
> NGINX_SSL_PATH=/etc/nginx/ssl  

7.3. After that you need create directories shown in .env with previlages on server:   

<!--
7.3.1. Create user on server for docker user   
> $ sudo useradd nginx   
> $ sudo useradd appuser   
> $ sudo useradd postgres   

7.3.2. Add main user to the new user group
> $ sudo usermod -aG nginx nonroot   
> $ sudo usermod -aG appuser nonroot   
> $ sudo usermod -aG postgres nonroot  

Ckeck main user groups
> $ groups nonroot
-->

7.3.3. Create dirs and change previlages   
> $ sudo mkdir -p /var/log/nginx && sudo chown nginx:nginx /var/log/nginx   
> $ sudo mkdir -p /etc/nginx/ssl
> $ sudo mkdir -p /var/log/gunicorn && sudo chown appuser:appuser /var/log/gunicorn   
> $ sudo mkdir -p /var/log/django && sudo chown appuser:appuser /var/log/django    
> $ sudo mkdir -p /usr/src/www/assets
> $ sudo mkdir -p /usr/src/www/media
> $ sudo mkdir -p /usr/src/www/static    
> $ sudo mkdir -p /var/lib/postgresql && sudo chown postgres:postgres /var/lib/postgresql   


7.3.4. Add SSL serts into /etc/nginx/ssl

create dirs for works
> sudo chmod u=rwx,g=rwx,o=rwx /var/log/nginx  
> sudo chmod u=rwx,g=rwx,o=rwx /var/log/gunicorn  
> sudo chmod u=rwx,g=rwx,o=rwx /var/log/django   
> sudo chmod u=rwx,g=rwx,o=rwx /var/lib/postgresql   
> sudo chmod u=rwx,g=rwx,o=rwx /var/lib/postgresql/data
> sudo chmod u=rwx,g=rwx,o=rwx /usr/src/www/assets
> sudo chmod u=rwx,g=rwx,o=rwx /usr/src/www/media
> sudo chmod u=rwx,g=rwx,o=rwx /usr/src/www/static


allow ip of host for django 79.143.29.118
docker-compose -f docker-compose.yml exec web python manage.py migrate



8. Running project
docker-compose up -d
