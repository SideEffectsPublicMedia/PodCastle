#!/bin/sh
# Server-side pull, publish and log.
/root/.virtualenvs/pc-sfx/bin/python manage.py pull_episodes
/root/.virtualenvs/pc-sfx/bin/python manage.py build
/root/.virtualenvs/pc-sfx/bin/python manage.py publish
