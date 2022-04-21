# n7gg

URL service, you probably don't want it.

Listens on :4242, and vends redirects or text responses for a static set
of keys, and 404's for everything else. Updating the set of known keys
currently requires updating `app.py` and restarting the service.

May someday read keys from a config file at startup maybe. /shrug


Usage
-----

Use the script:

    $ ./run.sh

Alternately, edit and install `n7gg.service` with systemd to exec `run.sh`.


License
-------

n7gg is copyright [John Reese](https://jreese.sh), and licensed under
the MIT license.  I am providing code in this repository to you under an open
source license.  This is my personal repository; the license you receive to
my code is from me and not from my employer. See the `LICENSE` file for details.
