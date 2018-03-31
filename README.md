# My Restaurants' Catalogue (App) - Amazon Web Services

This project is the extension of my existing project - [My Restaurants' Catalogue Web app](https://github.com/bethirahul/Restaurant-Web-app).
Built by _**Rahul Bethi**_.

It is a **Web application** hosted on [**Amazon Web Services (AWS)**](https://aws.amazon.com/) [**LightSail**](https://aws.amazon.com/lightsail/) [_Ubuntu_](https://www.ubuntu.com/) instance. It has a web server ([**Apache 2**](https://httpd.apache.org/)) with a database ([**PostgreSQL**](https://www.postgresql.org/)) to store and edit information about Restaurants and the food items sold in them.
It also has a user system with [_Google_](https://developers.google.com/identity/protocols/OAuth2) and [_Facebook_](https://developers.facebook.com/docs/facebook-login) [**OAuth 2.0 authentication**](https://oauth.net/2/) to login and make modifications ([**CRUD operations**](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)) to _add_, _edit_ or _delete_ restaurants and their items.

It also has a [JSON](https://www.json.org/) endpoint to provide restaurant details and item details.

## Built using

- [**Python 3.5.2**](https://www.python.org/) - [**Flask 0.12.2**](http://flask.pocoo.org/) micro-framework, [**SQLAlchemy 1.2.6**](https://www.sqlalchemy.org/), [**OAuth2client 4.1.2**](https://pypi.python.org/pypi/oauth2client)
- [**Apache 2.4.18**](https://httpd.apache.org/) web server
    - [``mod_wsgi`` 4.3.0](https://modwsgi.readthedocs.io/en/develop/) package
- [**PostgreSQL 9.5.12**](https://www.postgresql.org/) database server
- [**Ubuntu 16.04 LTS**](http://releases.ubuntu.com/16.04/) linux operating system
    - [Git](https://git-scm.com/), [Open**SSH**](https://www.openssh.com/) with key pairs, [Curl](https://curl.haxx.se/docs/manpage.html)
- [**Amazon Web Services (AWS)**](https://aws.amazon.com/) - [**LightSail**](https://aws.amazon.com/lightsail/) virtual machine instance on AWS Cloud
    - _Configuration_: 1 virtual CPU, 512 MB RAM, 20GB SSD
    - Same as AWS - EC2 instance, but with lower configuration, cheaper pricing and free tier.
    - Hosted at [**52.40.101.245**.xip.io](http://52.40.101.245.xip.io)
- [**Google**](https://developers.google.com/identity/protocols/OAuth2), [**Facebook**](https://developers.facebook.com/docs/facebook-login) [OAuth 2.0 authentication](https://oauth.net/2/) systems
- **HTML**, **CSS**
- Other tools used while building:
    - [**Vagrant 2.0.3**](https://www.vagrantup.com/) - [Ubuntu 16.04 LTS](http://releases.ubuntu.com/16.04/) Linux instance - local virtual machine
    - Windows 10 PC, Visual Studio Code
    - [Git-bash](https://git-scm.com/) to access AWS LightSail instance, [GitHub](https://github.com/)
    

## Instructions to run

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