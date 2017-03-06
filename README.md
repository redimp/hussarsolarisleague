Hussar Solairs League
=====================

The Hussar Solaris League (hsl) is a small tool, that provides an interface
for a 1 vs 1 League in Mechwarrior online. It was hacked on a gray
afternoon by <mail@redimp.de>. Provided without warranty of any kind.


Run in development mode
-----------------------

First, create `hsl/config.py` using `hsl/config.py.skeleton`. Second, create
the Databse in `hsl/hsl.sqlite` using e.g. `sqlite3 hsl/hsl.sqlite < notes/setup.sql`.

    python run.py

The best way for testing, set `REGISTER_ENABLED=True` and `TEST_MODE=True`.
You can create the test user with `sqlite3 hsl/hsl.sqlite < notes/testmode.sql`.

