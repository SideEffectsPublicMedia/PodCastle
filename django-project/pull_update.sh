#!/bin/sh
# Server-side pull, publish and log.
/root/.virtualenvs/pc-sfx/bin/python manage.py pull_episodes 2>&1 | logger --tag "pc-sfx"
/root/.virtualenvs/pc-sfx/bin/python manage.py build 2>&1 | logger --tag "pc-sfx"
/root/.virtualenvs/pc-sfx/bin/python manage.py publish 2>&1 | logger --tag "pc-sfx"
