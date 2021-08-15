WELLCOME!
---

It is project of the my site with blog. Site Powered on Django framework.  
You need use some linux distribution kit, in my case I use remote server based on Ubuntu 20.10.  
You can use the source code if you want for free.   
But please do not use information from my cv, and rename blog page ([ Я : blognote ]) =).  
If you want only check how to work project without deploying to server, then see 6 paragraph.  
 []
------------

# INSTALATION

1. Security setups  
1.0. Connect to server by SSH.  
1.1. Add new sudo user   
>```console
> $ useradd nonroot   
> $ passwd nonroot  
> New password:  
> Retype new password:  
> passwd: password updated successfully  
> ```

1.2. Add user to sudorer user group
> ```console
> serv:~# usermod -aG sudo nonroot
> ```

1.3. Check privileges  
>```console
> $ su - nonroot   
> $ sudo ls -l /root  
> total 0  
> ```

1.4. Add home directory with .ssh dir and authorized_keys file for nonroot user
>```console
> $ sudo mkhomedir_helper nonroot
> $ vi ~/.ssh/authorized_keys
>```

Enter the SSH public key or if you already using public key by root user see steps below.
>```console
> $ su root
> $ cat /root/.ssh/authorized_keys > /home/nonroot/.ssh/authorized_keys
> $ su nonroot
>```

Now check connection from other the Terminal, and then do next steps, or fix issue.

1.5.Change settings in sshd config file  
>```console
> $ vi /etc/ssh/sshd_config  
>```

Search and change:  
>```console
> PasswordAuthentication no  
> PermitRootLogin no  
> Port 55555  
>```
  
Number of port maybe any.  

1.6 Restart sshd  
>```console
> $ sudo service sshd restart  
>```


------------
2. Install general pakages

2.1. Type big string from here
>```console
> $ sudo apt-get update && sudo apt-get install -y vim zsh tmux htop git curl wget unzip zip gcc build-essential make w3m
>```


2.2. Change shell to zsh:
>```console
> $chsh -s $(which zsh)  
>```

Type zsh and tune zsh for you  
>```console
> zsh
>```

------------

3. Install Git
3.1. By default the linux distrs have Git, if not then do command:
>```console
> $ sudo apt install git
>```

------------ 
4. Install Docker
4.1. Prepere, install some the packages and do settings   
>```console
> $ sudo apt install apt-transport-https ca-certificates software-properties-common  
> $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  
> $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"  
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

------------

5. Install Docker-compose
5.1. Check last version on https://github.com/docker/compose/releases

5.2. Get and install:
>```console
> $ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
>```

5.3. Do executable:
>```console
> sudo chmod +x /usr/local/bin/docker-compose
>```

5.4. Check:
>```console
> $ docker-compose --version
>```

6. Install project from github
6.1. First create project directory and go to there:
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
7.1. Create .env file with environments setting in /usr/src/apps/my_cv_blog_2  
>```console
> $ sudo touch .env && sudo vim .env   
>```

7.2. Add environments values in .env-file:    
>```console
> DB_NAME=  
> DB_USER=  
> DB_PW=    
> DJANGO_ENV_ALLOWED_HOSTS=   
> DJANGO_ENV_SECRET_KEY=   
> DJANGO_ENV_EMAIL_HOST=   
> DJANGO_ENV_EMAIL_PORT=   
> DJANGO_ENV_EMAIL_HOST_USER=    
> DJANGO_ENV_EMAIL_HOST_PASSWORD=   
>```

P.S. For generating django secret key you can use some generator from search in Google, 
like https://djecrety.ir/ or 
https://stackoverflow.com/questions/41298963/is-there-a-function-for-generating-settings-secret-key-in-django

7.3. Create dirs for using in project   
For  project use into docker container id for :    
Run bash-script from app directory:   
>```console
> $ sudo ./scripts/init_dirs.sh   
>```

After will be create and configure dirs:    
- /var/lib/postgresql   
- /var/log/django   
- /var/log/gunicorn   
- /var/log/nginx   
- /usr/src/www/assets   
- /usr/src/www/media    
- /usr/src/www/static     


7.4. Initialize the nginx.conf file 

If you use SSL the command:   
>```console
> $ sudo ./scripts/init_nginx_conf.sh --ssl prefix
>```

!!!Place prefix yours sertificate prefix-file name wich you want copy to /etc/nginx/ssl.

Script create ssl-dir on path /etc/nginx/ssl and create nginx.conf file with prefix for .crt-file.
After copy your ssl sert (.crt-file) to /etc/nginx/ssl on your server.

If you do not want use SSL, then do command:
>```console
> $ sudo ./scripts/init_nginx_conf.sh --nossl
>```
Script create nginx.conf file without using ssl.

docker-compose -f docker-compose.yml exec web python manage.py migrate
 
8. Running project
docker-compose up -d
