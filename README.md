THE PERSONAL SITE WITH BLOG
---
Project state:  work in progress

Description:
It is source code of [my site](https://iakovenko.tech).
I used Django framework for web-app and Docker conteiners for continuous delivery: Nginx, Apps(Python3,
 Django, Gunicorn), Postgres.
Host mashine of site based on the Linux, in my case I use Ubuntu 20.04, all instruction for run based on it version.

Let's start:
If you want only check how to work project without deploying to server and you have installed Docker/Docker-compose and curl, then start from 6 paragraph.


Please check and give me feedback.

---
INSTALATION
------------

All opeartion executed in the shell. 

1. Security setups  
1.0. Connect to server by SSH.  
1.1. Add new sudo user   

>```console   
> $ useradd nonroot   
>```   

>```console   
> $ passwd nonroot   
>```   
   
>```console   
> New password:  
> Retype new password:  
> passwd: password updated successfully  
>```   
    
1.2. Add user to sudorer user group and create home directory 

>```console   
> $ usermod -aG sudo nonroot   
>```   

>```console    
> sudo mkhomedir_helper nonroot 
>```

1.3. Check privileges    

>```console   
> $ su - nonroot    
>```   
   
>```console    
> $ sudo ls -l /root  
> total 0
>```    


1.4. Add the ~/.ssh directory with authorized_keys file 
   
>```console   
> $  mkdir /home/nonroot/.ssh && touch /home/nonroot/.ssh/authorized_keys  
>```   

1.4.1. For add public key in authorized_keys use command:   
>```console
> $ vi ~/.ssh/authorized_keys
>```

1.4.2. If you already using public key by root user, you can copy key for *nonroot* user.

>```console
> $ sudo cat /root/.ssh/authorized_keys > /home/nonroot/.ssh/authorized_keys
>```

1.5. Change settings in sshd config file  
>```console
> $ sudo vi /etc/ssh/sshd_config  
>```

Search and change:  
>```console
> PasswordAuthentication no  
> PermitRootLogin no  
> Port 55555*  
>```
Save *sshd_config* file 
\* Number of port maybe any.  

1.6. Restart sshd  
>```console
> $ sudo service sshd restart  
>```

1.7. Check connection on SSH from other terminal through *nonroot* user.  

------------

2. Install general pakages   
2.1. Type big string from here   
>```console
> $ sudo apt-get update && sudo apt-get install -y vim zsh tmux htop git curl wget unzip zip gcc build-essential make w3m
>```

2.2. Change shell to zsh:   
>```console
> $ chsh -s $(which zsh)  
>```

Type zsh and tune zsh for you     
>```console
> $ zsh
>```

For your comfort you can install Oh-my-zsh:  
>```console
> $ sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
>```

------------

3. Install Git   
3.1. By default the linux distrs have Git, if it not then do command:  
>```console
> $ sudo apt install git
>```

------------ 

4. Install Docker  
4.1. Prepere, install some the packages and do settings   
>```console
> $ sudo apt install apt-transport-https ca-certificates software-properties-common  
>```

>```console
> $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  
>```

>```console
> $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"  
>```

>```console
> $ sudo apt update  
>```

4.2. Check place for download the docker package   
>```console
> $ apt-cache policy docker-ce
>```

4.3. Install docker   
>```console
> $ sudo apt install docker-ce
>```

4.4. Check status   
>```console
> $ sudo systemctl status docker
>```

4.5. Add current user to docker group   
>```console
> $ sudo usermod -aG docker ${USER}
>```

4.6. And last last step re-login in system and check Docker group for *nonroot* user
>```console
> $ su - nonroot
>```

>```console
> $ id
> uid=1000(nonroot) gid=1000(nonroot) groups=1000(nonroot),27(sudo),998(docker)
>```

------------

5. Install Docker-compose   
5.1. Check last version on https://github.com/docker/compose/releases   
5.2. Get and install:   
>```console
> $ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
>```

5.3. Do executable:   
>```console
> $ sudo chmod +x /usr/local/bin/docker-compose
>```   

5.4. Check:   
>```console
> $ docker-compose --version
>```

-----------

6. Install project from github   
6.1. First create project directory and go to it:   
>```console
> $ sudo mkdir -p /usr/src/apps/ && cd /usr/src/apps/
>```

6.2. Clone project from git   
>```console
> $ sudo git clone https://github.com/stalker24rus/my_cv_blog_2.git
>```

6.3. Check project   
>```console
> $ ls -l
>```

6.4. Go to my_cv_blog_2   
>```console
> $ cd my_cv_blog_2
>```

------------

7. Prepare system for working with project   
7.1. Create the .env file with environments settings in /usr/src/apps/my_cv_blog_2  
>```console
> $ sudo touch .env && sudo vim .env   
>```

7.2. Add environments values in a .env file:    
>```console
> DB_NAME=  
> DB_USER=  
> DB_PW=
> DJANGO_ENV_ADMIN_PAGE=    
> DJANGO_ENV_ALLOWED_HOSTS=   
> DJANGO_ENV_SECRET_KEY=   
> DJANGO_ENV_EMAIL_HOST=   
> DJANGO_ENV_EMAIL_PORT=   
> DJANGO_ENV_EMAIL_HOST_USER=    
> DJANGO_ENV_EMAIL_HOST_PASSWORD=   
> DJANGO_ENV_LOG_PATH=/var/log/django/
> DJANGO_ENV_WWW_PATH=/usr/src/www/
>```

For generating django secret key you can use some generator from search in Google, 
like https://djecrety.ir/ or 
https://stackoverflow.com/questions/41298963/is-there-a-function-for-generating-settings-secret-key-in-django

7.3. Create using dirs for project   
Run bash-script from current (/usr/src/apps/my_cv_blog_2) directory:   
>```console
> $ sudo ./scripts/init_dirs.sh   
>```

Then created dirs with permissions for user of Docker conteainer:    
- /var/lib/postgresql   
- /var/log/django   
- /var/log/gunicorn   
- /var/log/nginx   
- /usr/src/www/assets   
- /usr/src/www/media    
- /usr/src/www/static     


7.4. Initialize the nginx.conf file   

7.4.1. If you use SSL(for https) then run sh-script:   
>```console
> $ sudo ./scripts/init_nginx_conf.sh --ssl prefix
>```

!!!Replace prefix to yours sertificate prefix-file name, wich you want copy to /etc/nginx/ssl.

Script create ssl-dir on path /etc/nginx/ssl and create nginx.conf file with prefix for .crt-file.
After copy your ssl sert (.crt-file) to /etc/nginx/ssl.

7.4.2. If you do not want use SSL, then do command:
>```console
> $ sudo ./scripts/init_nginx_conf.sh --nossl
>```
Script create nginx.conf file without using ssl.

--- 

8. Run project   

8.1. Run container with builds:
>```console
> $ docker-compose up -d
>```

8.2. After build images and running containers, first need migrate Django data model for blog app 
to data base:

>```console
> $ docker-compose -f docker-compose.yml exec web python manage.py makemigrations blog && docker-compose -f docker-compose.yml exec web python manage.py migrate
>```

8.3. Create super-user for postgres data base:
>```console
> $ docker-compose -f docker-compose.yml exec web python manage.py createsuperuser
>```

8.4. Collect project static files

>```console
> $ docker-compose -f docker-compose.yml exec web python manage.py collectstatic
>```

8.5 Open site in browser by IP.
