#!/bin/sh
# Server-side pull, publish and log.
source /root/.bashrc
/root/.virtualenvs/pc-sfx/bin/python /root/sfx-pc/django-project/manage.py pull_episodes
/root/.virtualenvs/pc-sfx/bin/python /root/sfx-pc/django-project/manage.py build
/root/.virtualenvs/pc-sfx/bin/python /root/sfx-pc/django-project/manage.py publish

*/15 * * * * sh /root/sfx-pc/django-project/pull_update.sh 2>&1 | logger --tag "pc-sfx"