======================================
How to deploy Etherpad on DreamCompute
======================================

Etherpad is a web application that lets you collaborate with others in a text
editor, much like an open source Google Docs alternative.

Setting up a server
~~~~~~~~~~~~~~~~~~~

The first step to deploying Etherpad is to launch a server to run it on. For
example in this tutorial, an Ubuntu Xenial server is used. View the following
link for documentation on how to do this.
https://help.dreamhost.com/hc/en-us/articles/215912848-How-to-launch-and-manage-servers-with-the-DreamCompute-dashboard.
You also need to expose port 8080 to incoming traffic,
as that is blocked by default. View the following link for documentation on how
to add security rules.
https://help.dreamhost.com/hc/en-us/articles/215912838-How-to-configure-access-and-security-for-DreamCompute-instances

Installing dependencies
~~~~~~~~~~~~~~~~~~~~~~~

Once you have your server up and running the next step is to install all of
Etherpad's dependencies:

.. code:: bash

    apt-get install gzip git curl python libssl-dev pkg-config build-essential
    apt-get install nodejs npm

Next you must symlink /usr/bin/nodejs to /usr/bin/node because Etherpad will
try to use that path. Most Linux distributions install nodejs in /usr/bin/node.
This step is only necessary on Ubuntu servers since it doesn't install nodejs
in /usr/bin/node because of another package.

.. code:: bash

    ln -s /usr/bin/nodejs /usr/bin/node

Installing Etherpad
~~~~~~~~~~~~~~~~~~~

Now that all the dependencies are installed the next step is to download
Etherpad and run it. To clone Etherpad using git, run:

.. code:: bash

    git clone git://github.com/ether/etherpad-lite.git

Configuration
-------------

Networking
^^^^^^^^^^

Now comes the configuration of Etherpad. By default it runs on port 9001.
Change it to run on port 8080 by editing the settings.json file:

.. code:: bash

    "port" : 9001,

should be changed to:

.. code:: bash

    "port" : 8080,

.. Note::

    See the following link for how to expose port 8080 to incoming traffic.
    https://help.dreamhost.com/hc/en-us/articles/215912838-How-to-configure-access-and-security-for-DreamCompute-instances

Database
^^^^^^^^

By default Etherpad uses dirtyDB to store its data, but it's recommended you
use something else in a production environment and only use dirtyDB for
testing. This tutorial uses MySQL to store data, but Etherpad supports other
databases such as PostgreSQL and SQLite.

If you don't have MySQL running, follow `this <215879487>`__. Once you have
that running, connect to MySQL and create a database for Etherpad to use:

.. code:: bash

    $ mysql -u root -p
    Enter password:
    mysql> CREATE DATABASE etherpad

Finally edit settings.json and delete the configuration for dirtyDB:

.. code:: bash

    "dbSettings" : {
                   "filename" : "var/dirty.db"
                   },

And add the configuration for MySQL:

.. code:: bash

    "dbType" : "mysql",
    "dbSettings" : {
                     "user"    : "etherpad",
                     "host"    : "localhost",
                     "password": "ETHERPAD USER PASSWORD",
                     "database": "etherpad",
                     "charset" : "utf8mb4"
                   },

Your configuration may be a bit different depending on how you have MySQL
configured, adjust the values accordingly.

Starting Etherpad
~~~~~~~~~~~~~~~~~

Now that everything is configured, you can finally start Etherpad. I recommend
running it inside screen or tmux so that it continues to run after you
disconnect from the server.

.. code:: bash

    tmux
    bin/run.sh

Etherpad is now running. Confirm it works by going to http://IP:8080. Make
sure to replace "IP" with the IP address of your server.

.. meta::
    :labels: etherpad
