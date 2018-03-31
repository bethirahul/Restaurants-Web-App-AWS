# My Restaurants' Catalogue (App) - Amazon Web Services

Application link: http://52.40.101.245.xip.io/restaurants_catalogue

This project is the extension of my existing project - [**My Restaurants' Catalogue**](https://github.com/bethirahul/Restaurant-Web-app).
Built by _**Rahul Bethi**_.

It is a **Web application** hosted on [Amazon Web Services (AWS)](https://aws.amazon.com/) [LightSail](https://aws.amazon.com/lightsail/) Ubuntu instance. It has a web server (Apache 2) with a database (PostgreSQL) to store and edit information about **Restaurants** and the **food items** sold in them.
It also has a user system with [_Google_](https://developers.google.com/identity/protocols/OAuth2) and [_Facebook_](https://developers.facebook.com/docs/facebook-login) - [OAuth 2.0](https://oauth.net/2/) authentication to login and make modifications (CRUD operations) to _add_, _edit_ or _delete_ restaurants and their items.

It also has a JSON endpoint to provide restaurant details and item details.

## Built using

1. [**Python**](https://www.python.org/) v3.5.2 - [**Flask**](http://flask.pocoo.org/) v0.12.2 (_micro-framework_), [SQLAlchemy](https://www.sqlalchemy.org/) v1.2.6, [OAuth2client](https://pypi.python.org/pypi/oauth2client) v4.1.2
2. [**Apache**](https://httpd.apache.org/) v2.4.18 web server
    - [mod_wsgi](https://modwsgi.readthedocs.io/en/develop/) v4.3.0 package
3. [**PostgreSQL**](https://www.postgresql.org/) v9.5.12 database server
4. [Ubuntu 16.04 LTS](http://releases.ubuntu.com/16.04/) linux operating system
    - [Git](https://git-scm.com/), [OpenSSH](https://www.openssh.com/) with key pairs, [Curl](https://curl.haxx.se/docs/manpage.html)
5. [**Amazon Web Services**](https://aws.amazon.com/) (AWS) - [LightSail](https://aws.amazon.com/lightsail/) virtual machine instance on AWS Cloud
    - Lower configuration than a AWS EC2 _t2-micro_ instance (512MB RAM), cheaper pricing and free tier.
    - Hosted at [**52.40.101.245**.xip.io](http://52.40.101.245.xip.io)
6. [**Google**](https://developers.google.com/identity/protocols/OAuth2), [**Facebook**](https://developers.facebook.com/docs/facebook-login) - [OAuth 2.0](https://oauth.net/2/) authentication systems
7. HTML, CSS
8. Other tools used while developing (not needed to build the app again):
    - [**Vagrant**](https://www.vagrantup.com/) v2.0.3 virtual machine - identical to AWS instance
        - Used to test and debug the app in the local machine, before setting the app on AWS Cloud.
    - Windows 10 PC, Visual Studio Code
    - [Git-bash](https://git-scm.com/) to access AWS LightSail instance, [GitHub](https://github.com/)

## Instructions to run

### Setup system

1. Get an [**AWS** account](https://portal.aws.amazon.com/billing/signup?redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) (free tier) and create a [**LightSail**](https://lightsail.aws.amazon.com/ls/webapp/home/instances) instance with '_OS only (Ubuntu 16.04 LTS)_' option.
2. Create a _Static IP address_ from ``AWS LightSail console -> Networking`` and attach it to the instance created.
3. Open the instance from the AWS console (opens in browser) or by SSH into the instance by using username ``ubuntu``, instance's IP address and SSH private key location .
    - _AWS default SSH key_ can be obtained from ``AWS LightSail console -> Account -> SSH Keys``.
4. Create a **new user** and add ``sudo`` permission by adding an entry in ``/etc/sudoers.d/<new_file>``
    - Create a new **SSH key pair** using ``ssh-keygen`` on the local machine.
    - Copy the SSH public key into new user's ``/home/<new_user>/.ssh/authorized_keys`` file in the AWS instance.
    - Change file permissions and ownership on the ``authorized_keys`` file and ``.ssh`` directory.
        ```bash
        sudo chmod 600 /home/<new_user>/.ssh/authorized_keys
        sudo chmod 700 /home/<new_user>/.ssh
        sudo chown <new_user> /home/<new_user>/.ssh/authorized_keys
        sudo chown <new_user> /home/<new_user>/.ssh
        sudo chgrp <new_user> /home/<new_user>/.ssh/authorized_keys
        sudo chgrp <new_user> /home/<new_user>/.ssh
        ```
    - Now this user on AWS instance can be logged in from this local machine using the username, IP address of the instance and the SSH private key on the local machine.
        ```bash
        ssh <new_user>@<ip_address-or-server_address> -p <ssh_port> -i /private/key/location/with/file
        ```
5. Close and login with the new user.
6. Update the system.
    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    ```
7. Install **Finger** to check more details about a user
    - Install: ``sudo apt-get finger``
    - Current user info: ``finger``
    - User info (detailed): ``finger <user>``
8. Modify SSH configuration file ``/etc/ssh/sshd_config``
    - Disable _Login-by-password_ by changing ``PasswordAuthentication`` to ``no``
    - Change **SSH port**
        - First Allow AWS LightSail instance's Firewall to allow/deny the desired ports ``AWS LightSail console -> Instance -> Networking -> Firewall``.
        - Change ``Port`` to your desired port number in the configuration file.
    - Restart SSH ``sudo service sshd restart``
9. Configure **Uncomplicated FireWall** (UFW) to allow SSH (new port), HTTP(80) and NTP(123) ports.
    - Check status: ``sudo ufw status``
    - Deny all incoming: ``sudo ufw default deny incoming``
    - Allow all outgoing: ``sudo ufw default allow outgoing``
    - Allow port: ``sudo ufw allow <port#>``
    - Allow port on TCP or UDP: ``sudo ufw allow <port#>/<tcp-or-udp>``
    - Allow changed SSH port and NTP using their port numbers as shown above.
    - HTTP can also be allowed by using names ``www`` or ``http``
        - ``sudo ufw allow www`` or ``sudo ufw allow http``
10. Configure the local time-zone to UTC.
    - Run ``sudo dpkg-reconfigure tzdata``
    - Then select ``None of the above -> UTC``

### Install softwares

1. Install [**Python 3.5**](https://www.python.org/downloads/), and then ``pip install``:
    - ``flask``
    - ``sqlalchemy``
    - ``oauth2client``
    - ``httplib2``
2. Setup Database:
    - _Skip this step and delete [``restaurantmenuwithusers.db``](/restaurantmenuwithusers.db) file if you want to use my database setup_
    - Run [``database_setup.py``](/database_setup.py) using Python to setup Database
    - Run [``initiating_db_with_users.py``](/initiating_db_with_users.py) using Python to populate the database with values.
        - _You can modify this file with your own values._
3. Run [``flask_app.py``](/flask_app.py) using Python, the app will be up and running on [localhost:8000](http://localhost:8000) address. Press **Ctrl**+**C** a few times to stop the server.
4. To be able to use Google and Facebook OAuth 2.0 Authentication, App ID and Client Secret are needed from each of the providers.
    - For Google - Create App Credentials at [Google's Developers webpage](https://console.developers.google.com) and download the clients secret JSON file into the project. Rename it to ``client_secrets.json``.
        - A Mockup of the client secrets json file is already present with other credentials in it [``client_secrets.json``](/client_secrets.json). GO through it to setup credentials at google and replace it with your own ``client_secrets.json`` file.
    - For Facebook - Goto [Facebook's Developers webpage](https://developers.facebook.com/) and create AppCredentials. Copy the App ID and App Secret into the [``fb_client_secrets.json``](/fb_client_secrets.json) file.
5. There are two type of JSON endpoints for restaurants.
    - [``/restaurants/json``](http://localhost:8000/restaurants/json) - for all restaurnts' _name_, _ID_ and _creater ID_
    - ``/restaurants/``_\<``Restaurant ID``>_``/json`` - for each restaruant's items

## Design

1. [``database_setup.py``](/database_setup.py) uses SQLAlchemy library to setup database and tables inside it.
    - It has classes for tables and Columns in each table.
    - Serialize function in each class to return items in easily readable format - to convert to json.
    - Menu Item class also has time variable which stores the time when the item is created. This is used to sort the latest added items.

2. [``initiating_db_with_users.py``](/initiating_db_with_users.py) is used to populate the empty database which was created.

3. The server code [``flask_app.py``](/flask_app.py) is the main program.
    - It handles all the requests from the client, including Google and Facebook _OAuth 2.0_ Authentication.
        - Files [``client_secret.json``](/client_secret.json) for Google and [``initiating_db_with_users.py``](/initiating_db_with_users.py) for Facebook are used get the App ID and Client Secret for respective providers.
        - A Random string is generated and used to send and receive as state_token to avoid _Cross-site Reference Forgery attacks_.
        - When a user log-in for the first time, A new entry is created in the database by getting the details of user's _name_, _profile picture_, _email_ and _ID_.
        - A returning user is identified using his _email_ address.

    - It also handles _CRUD operations_ (using SQLAlchemy) on the database which we created, based on the requests we get from client.
    - Two _Methods_ are supported, GET and POST as HTML5 only supports these two.
        - All links are accessed through GET method, only CRUD operations and login pages use POST method to submit the requests.

    - Flask framework is used to _handle requests_, send _**Flash messages**_ for errors, and render _**Dynamic HTML webpages**_.
        - The HTML templates are located in [templates](/templates) folder.
        - CSS style sheet [``styles.css``](/static/styles.css) is located in [static](/ststic) folder

    - And at last the web server is run on [localhost:8000](http://localhost:8000) address.

_Please read through the detailed code comments in [``flask_app.py``](/flask_app.py) to know how the app is built._

**Screenshots** of all the pages are located in [Screenshots](/Screenshots) folder.

#### My LinkedIn profile

https://www.linkedin.com/in/rahulbethi