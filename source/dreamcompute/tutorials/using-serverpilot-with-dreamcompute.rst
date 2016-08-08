==============================================================
Registering a DreamCompute server with ServerPilot using Shade
==============================================================

This article assumes you have a clouds.yaml file that has the information on
how to authenticate to your DreamCompute account. It also assumes that you
already have an account on ServerPilot and have your client ID and API key for
that account.

Getting a server ID and server API key from ServerPilot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first step in this process is to request a new server ID and server API
key from ServerPilot. We'll also set the name of the server we want to create
here.

.. literalinclude:: examples/serverpilot.py
    :start-after: step-1
    :end-before: step-2

Next we make the reques to the ServerPilot API to create new a new server ID
and API key.

.. literalinclude:: examples/serverpilot.py
    :start-after: step-2
    :end-before: step-3

Now we have a server ID and server API key stored in the ``response_json``
dictionary that we can use with the server we want to register with
ServerPilot.

Launching a server and registering it with ServerPilot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next we launch the server and run the ServerPilot installer on it.

First we must pass the ServerPilot to the server to run at creation

.. literalinclude:: examples/serverpilot.py
    :start-after: step-3
    :end-before: step-4

Next set variables for the image, flavor, and key pair to launch the server
with.

.. literalinclude:: examples/serverpilot.py
    :start-after: step-4
    :end-before: step-5

Change the ``key_name`` file to be the name of your key pair on DreamCompute so
that you can SSH into the server. The ``image`` and ``flavor_id``
variables can also be modified to deploy a different image or a different size
server.

Finally, connect to DreamCompute with Shade and request that the server we want
be built. For more information about Shade, read our documentation on how to
use Shade with DreamCompute `here <214836997>`__.

.. literalinclude:: examples/serverpilot.py
    :start-after: step-5

Once the script runs and finishes, go to ServerPilot.com, click on servers
and you should see your new server (it may take up to a couple minutes for the
installation script to finish). You can now use ServerPilot to manage your
server and deploy applications on it.

Full script
~~~~~~~~~~~

.. literalinclude:: examples/serverpilot.py

.. meta::
    :labels: serverpilot
