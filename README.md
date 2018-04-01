# My Restaurants' Catalogue (App) - Amazon Web Services

Application link: http://52.40.101.245.xip.io/restaurants_catalogue

This project is the extension of my existing project - [**My Restaurants' Catalogue**](https://github.com/bethirahul/Restaurant-Web-app).
Built by _**Rahul Bethi**_.

It is a **Web application** hosted on [Amazon Web Services (AWS)](https://aws.amazon.com/) [LightSail](https://aws.amazon.com/lightsail/) Ubuntu instance. It has a web server (Apache 2) with a database (PostgreSQL) to store and edit information about **Restaurants** and the **food items** sold in them.
It also has a user system with [_Google_](https://developers.google.com/identity/protocols/OAuth2) and [_Facebook_](https://developers.facebook.com/docs/facebook-login) - [OAuth 2.0](https://oauth.net/2/) authentication to login and make modifications (CRUD operations) to _add_, _edit_ or _delete_ restaurants and their items.

It also has a JSON endpoint to provide restaurant details and item details.

## Built using

1. [**Python**](https://www.python.org/) v3.5.2
    - [**Flask**](http://flask.pocoo.org/) v0.12.2 - micro-framework
    - [SQLAlchemy](https://www.sqlalchemy.org/) v1.2.6 - SQL toolkit
    - [OAuth2client](https://pypi.python.org/pypi/oauth2client) v4.1.2 - OAuth 2.0 client library
    - [Psycopg2](http://initd.org/psycopg/) v2.7.4 - PostgreSQL adapter
2. [**Apache**](https://httpd.apache.org/) v2.4.18 web server
    - [mod_wsgi](https://pypi.python.org/pypi/mod_wsgi) v4.3.0 - Apache module for [WSGI](https://www.python.org/dev/peps/pep-3333/) compliant interface
3. [**PostgreSQL**](https://www.postgresql.org/) v9.5.12 database server
4. [Ubuntu 16.04 LTS](http://releases.ubuntu.com/16.04/) linux operating system
    - [Git](https://git-scm.com/), [OpenSSH](https://www.openssh.com/) with key pairs, [Curl](https://curl.haxx.se/docs/manpage.html)
5. [**Amazon Web Services**](https://aws.amazon.com/) (AWS) - [LightSail](https://aws.amazon.com/lightsail/) virtual machine instance on AWS Cloud
    - Lower configuration than a AWS EC2 _t2-micro_ instance (512MB RAM), cheaper pricing and free tier.
    - Hosted at [**52.40.101.245**.xip.io](http://52.40.101.245.xip.io)
6. [**Google**](https://developers.google.com/identity/protocols/OAuth2), [**Facebook**](https://developers.facebook.com/docs/facebook-login) - [OAuth 2.0](https://oauth.net/2/) authentication systems
7. HTML, CSS
8. Xip.io DNS
9. Other tools used while developing (not needed to build the app again):
    - [**Vagrant**](https://www.vagrantup.com/) v2.0.3 virtual machine - identical to AWS instance
        - Used to test and debug the app in the local machine, before setting the app on AWS Cloud.
    - Windows 10 PC, Visual Studio Code
    - [Git-bash](https://git-scm.com/) to access AWS LightSail instance, [GitHub](https://github.com/)
    - [**Finger**](https://www.lifewire.com/finger-linux-command-4093522), to get more information on a user.

## Instructions to run

### Setup system

1. Get an [**AWS** account](https://portal.aws.amazon.com/billing/signup?redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) (free tier) and create a [**LightSail**](https://lightsail.aws.amazon.com/ls/webapp/home/instances) instance with '_OS only (Ubuntu 16.04 LTS)_' option.
2. Create a _Static IP address_ from [AWS LightSail console] -> [Networking] and attach it to the instance created.
3. Open the instance from the [AWS LightSail console] (opens in browser) or by SSH into the instance by using username ``ubuntu``, instance's IP address and SSH private key location.
    - _AWS default SSH key_ can be obtained from [AWS LightSail console] -> [Account] -> [SSH Keys].
4. Create a **new user** and add ``sudo`` permission.
    - New user:
        - ``sudo useradd`` _``<new_user>``_
    - Add sudo permission by adding an entry in a _new file_ at ``/etc/sudoers.d/``_``<new_user>``_
        - _``<new_user>``_ ``ALL=(ALL) NOPASSWD:ALL``
    - Create a new **SSH key pair** by running ``ssh-keygen`` on the local machine.
    - Copy the SSH public key into new user's ``/home/``_``<new_user>``_``/.ssh/authorized_keys`` file in the AWS instance.
        - Create the directory and file if they don't exist.
    - Change file permissions and ownership on the ``authorized_keys`` file and ``.ssh`` directory.
        ```bash
        sudo chmod 600 /home/<new_user>/.ssh/authorized_keys
        sudo chmod 700 /home/<new_user>/.ssh
        sudo chown <new_user> /home/<new_user>/.ssh/authorized_keys
        sudo chown <new_user> /home/<new_user>/.ssh
        sudo chgrp <new_user> /home/<new_user>/.ssh/authorized_keys
        sudo chgrp <new_user> /home/<new_user>/.ssh
        ```
    - Now, this user on AWS instance can log in from this local machine using the username, IP address of the instance and the SSH private key on the local machine.
        - ``ssh`` _``<new_user>``_``@``_``<ip_address-or-domain>``_ ``-p <ssh_port> -i`` _``/private/key/location/with/file``_
5. Close and login with the new user.
6. **Update** the system.
    - ``sudo apt-get update`` --> Check for updates
    - ``sudo apt-get upgrade`` --> Updates system
    - If you still have packages to upgrade, use
        - ``sudo apt-get dist-upgrade`` --> Updates dependencies too
7. Modify **SSH configuration** file ``/etc/ssh/sshd_config``
    - Disable _Remote-root-login_ by changing ``PermitRootLogin`` to ``no``
    - Disable _Login-by-password_ by changing ``PasswordAuthentication`` to ``no``
    - Change **SSH port**
        - First Allow AWS LightSail instance's Firewall to allow/deny the desired ports [AWS LightSail console] -> [Instance] -> [Networking] -> [Firewall].
        - Change ``Port`` to your desired port number in the configuration file.
    - Restart SSH ``sudo service sshd restart``
8. Configure **Uncomplicated FireWall** (UFW) to allow SSH (new port), HTTP(80) and NTP(123) ports.
    - Check status: ``sudo ufw status``
    - ``sudo ufw default deny incoming`` --> Deny all incoming
    - ``sudo ufw default allow outgoing`` --> Allow all outgoing
    - ``sudo ufw allow`` _``<port#>``_ --> Allow port
    - ``sudo ufw allow`` _``<port#>``_``/``_``<tcp-or-udp>``_ --> Allow port on TCP or UDP
    - Allow changed SSH port and NTP using their port numbers as shown above.
    - HTTP can also be allowed by using names ``www`` or ``http``
        - ``sudo ufw allow www`` or ``sudo ufw allow http``
9. Configure the **Local time-zone** to UTC.
    - Run ``sudo dpkg-reconfigure tzdata``
    - Then select [None of the above] -> [UTC]

### Install software

1. Install **Apache2** web server
    - ``sudo apt-get install apache2``
2. Install **PostgreSQL** database server
    - ``sudo apt-get install postgresql``
3. **Python 3.5.2** comes pre-installed on this instance, but not [**Pip**](https://pypi.python.org/pypi/pip). Pip is used to get python packages.
    - Install Pip: ``sudo apt-get install python3-pip``
4. Install Python packages
    - ``pip3 install flask`` --> **Flask** _(micro-framework)_
    - ``pip3 install sqlalchemy`` --> SQL toolkit
    - ``pip3 install oauth2client`` --> OAuth 2.0 client library
    - ``pip3 install psycopg2`` --> PostgreSQL database adapter
    - ``sudo apt-get install libapache2-mod-wsgi-py3`` --> Apache module (WSGI)

### Setup Database server

1. Change user to _postgres_ (default PostgreSQL user) - ``sudo su postgres``
2. Log into PostgreSQL server by running command: ``psql``
3. Create a new **database user** with only login permission.
    ``` SQL
    CREATE USER <user> WITH
        LOGIN
        NOSUPERUSER
        NOCREATEDB
        NOCREATEROLE
        INHERIT
        NOREPLICATION
        CONNECTION LIMIT -1
        PASSWORD '<password>';
    ```
4. Create **new database** with the _new user_ as its owner.
    ``` SQL
    CREATE DATABASE <database>
        WITH
        OWNER = <user>
        ENCODING = 'UTF8'tablespace
        CONNECTION LIMIT = -1;
    ```

### Setup Project

1. Clone this project into your _desired directory_. Goto the _desired directory_, then run:
    - ``git clone https://github.com/bethirahul/Restaurants-Web-App-AWS``
2. Create a _new file_ ``database_secrets.json`` in the project root folder and fill it up with database details (_user_, _password_ and _database_ which were created earlier), as shown here.
    ```json
    {
        "postgresql": {
            "user": "<database_user>",
            "password": "<password>",
            "database": "<database_name>"
        }
    }
    ```
3. To use **Google OAuth 2.0** authentication, goto [Google's Developers webpage](https://console.developers.google.com) and create new app (button on top).
    - Goto [Credentials] -> [Credentials] and create a new OAuth client ID. Open the client ID
        - Set Javascript Origins to ``http://``_``<server_ip_address>``_``.xip.io``
        - Set Redirect URIs to ``http://``_``<server_ip_address>``_``.xip.io/restaurants_catalogue/gconnect``
        - Get the client secrets by clicking [Download Json] button on the top. Place this file in the project root folder and rename it to ``client_secrets.json``.
    - Goto [Credentials] -> [OAuth consent screen] and set _Email_ and _Product Name_.
4. To use **Facebook OAuth 2.0** authentication, goto [Facebook's Developers webpage](https://developers.facebook.com/)
    - Goto [My Apps] (top right corner) and [Add a New App].
    - Goto [Add a Product] -> [Facebook Login] -> [Set Up]
    - Goto [Facebook Login] (left) -> [Settings] and set Redirect URIs to
        - ``http://``_``<server_ip_address>``_``.xip.io/restaurants_catalogue/fbconnect``
    - Goto [Settings] (left) -> [Basic]
        - Copy the App ID and App Secret into a new file named ``fb_client_secrets.json`` in the project root folder. Fill it up as shown here
            ```json
            {
                "web": {
                    "app_id": "<your_app_id>",
                    "app_secret": "<your_app_secret>"
                }
            }
            ```
5. Run [database_setup.py](database_setup.py) file using python 3, to setup the database with necessary tabels (with rows and columns).
    - ``python3 database_setup.py``
6. Run [initiating_db_with_users.py](initiating_db_with_users.py) to fill the database tables with some information, this is needed for the app to work.
    - ``python3 initiating_db_with_users.py``
    - You can modify this file or make another file by taking this file as a templete.
    - **_Note_:** Running the same file more than once without modifying, will add  duplicate entries into the database.

### Setup Apache web server

1. Create a new file at ``/etc/apache2/sites-available/``_``<new_conf_file>``_``.conf`` and fill it up by modifying the templete file [restaurants_app.conf](/apache/restaurants_app.conf)
2. Run command ``sudo a2ensite`` _``<new_conf_file>``_``.conf`` to let the apache server use the new configuration file.
    - To disable a configuration file, run ``sudo a2dissite`` _``<conf_file>``_``.conf``
3. Restart web server - ``sudo service apache2 reload``

## Design

This project is the extension of the Restaurant's web app. Hosting the app onto the web using a virtual machine on the cloud is done here.

1. A **AWS LightSail** virtual machine (VM) instance is setup with **Ubuntu 16.04 LTS** linux operating system.
2. A **Static IP** is created for that instance.
3. **Domain name** of the server is created using Xip.io, a free Public DNS server.
    - Any domain name can be created from an IP address by appending the IP address with ``.xip.io``
    - THe DNS server just redirects back the IP address.
4. A **new user** with is created and sudo permissions are assigned.
5. A new pair of **SSH Keys** are setup and are used between the host machine and the new user in the AWS VM. Login with password is disabled on the VM.
6. **SSH port** is changed as a precaution to stop attacks on the default port.
7. **AWS LightSail Firewall** is configured to allow this new port.
8. The **Uncomplicated FireWall** (UFW) on the VM is also setup to block all incoming ports except, the new SSH port, HTTP and NTP ports. All outgoing ports are allowed.
9. **Local time-zone** is set to UTC.
10. System is **updated** and all the necessary software and their packages are **installed**.
11. Application is cloned into a directory using **Git**.
12. **PostgreSQL database** server is configured by creating a new user and creating a new database with the owner of the new database being the new database. These details are stored in the ``database_secrets.json`` file, so that the app can use those details to access the database.
13. **Database is setup** with necessary tables by using the username, password and database name from the ``database_secrets.json`` file.
14. **Database is then populated** with some Restaurant names, item names and users.
15. **Google and Facebook app secrets** are taken and stored in their respective json files. These details are used by the app to login a user using **OAuth2.0** authentication.
16. Apache web server is configured by adding the app's apache configuration into the server's configuration folder. Then the server is updated with the new configuration file. Restart the server to take effect.

This makes the app run at ``http://``_``<server_ip_address>``_``.xip.io/restaurants_catalogue/``

Address to my hosted app: http://52.40.101.245.xip.io/restaurants_catalogue

**Screenshots** of all the pages are located in [Screenshots](/Screenshots) folder.

## References

1. [Udacity - Full Stack nano degree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) course
2. [Udemy - AWS Developer Associate](https://www.udemy.com/aws-certified-developer-associate/learn/v4/overview) course
3. [Google OAuth2](https://developers.google.com/identity/protocols/OAuth2) docs
4. [Facebook OAuth2](https://developers.facebook.com/docs/facebook-login/web) docs
5. [SSH](https://man.openbsd.org/sshd_config) configuration
6. [SSH Keygen](https://man.openbsd.org/ssh-keygen.1) docs
7. [UFW](https://help.ubuntu.com/community/UFW) configuration
8. [Apache](https://httpd.apache.org/docs/2.4/) configuration
9. [Apache mod_wsgi](http://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html) configuration
10. [PostgreSQL](https://www.postgresql.org/docs/9.5/static/index.html) docs
12. [``sudo``](https://linux.die.net/man/8/sudo) docs
13. [``apt-get``](https://linux.die.net/man/8/apt-get) docs
14. [``chmod``](https://linux.die.net/man/1/chmod) docs

## Contact me

Linkdin: https://www.linkedin.com/in/rahulbethi

Email: rahulbethi@hotmail.com

Phone: +1 (361) 336-7752
