#!/bin/sh
# Server-side pull, publish and log.
/root/.virtualenvs/pc-sfx/bin/python manage.py pull_episodes 2>&1 | logger &
