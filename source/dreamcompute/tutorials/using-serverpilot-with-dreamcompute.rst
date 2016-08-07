==============================================================
Registering a DreamCompute server with ServerPilot using Shade
==============================================================

This article assumes you have a clouds.yaml file that has the information on
how to authenticate to your DreamCompute account. It also assumes that you
already have an account on ServerPilot and have your client ID and API key for
that account.

Getting a serverid and serverkey from ServerPilot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first step in this process is to request a new server ID and server API
key from ServerPilot. This is so that we can run a script on the server that
registers our server with SeverPilot.

.. literalinclude:: examples/serverpilot.py
    :start-after: step-1
    :end-before: step-2

Set the ``client_id`` variable to your ServerPilot client ID and set the
``api_key`` to your ServerPilot API key.

Now we have a server ID and server API key stored in the ``response_json``
dictionary that we can use with the server we want to register with
ServerPilot.

Launching a server and registering it with ServerPilot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next we launch the server and run the ServerPilot installer on it.

.. literalinclude:: examples/serverpilot.py
    :start-after: step-2

Change the ``key_name`` file to be the name of your key pair on DreamCompute so
that you can SSH into the server. The ``image`` and ``flavor_id``
variables can also be modified to deploy a different image or a different size
server.

The ``userdata`` argument passed to the ``create_server`` function launches the
script we passed to it on creation of the instance using Cloud-Init, in this
case, we are passing it the ServerPilot installer with the server ID and api
key we obtained earlier.

Once the script runs and finishes, go to ServerPilot.com, click on servers
and you should see your new server (it may take up to a couple minutes for the
installation script to finish). You can now use ServerPilot to manage your
server and deploy applications on it.

Full script
~~~~~~~~~~~

.. literalinclude:: examples/serverpilot.py

.. meta::
    :labels: serverpilot
