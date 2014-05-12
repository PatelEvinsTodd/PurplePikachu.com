from __future__ import with_statement
from fabric.api import *

code_dir = '/var/www/PurplePikachu.com'

def dev():
    env.user = 'oak'
    env.hosts = ['pokemon.tannerevins.com']

def prod():
    env.user = 'oak'
    env.hosts = ['purplepikachu.com']

def deploy():
    with settings(warn_only=True):
        if run('test -d %s' % code_dir).failed:
            run('git clone https://github.com/PatelEvinsTodd/PurplePikachu.com %s' % code_dir)
    with cd(code_dir):
        run("git pull")

