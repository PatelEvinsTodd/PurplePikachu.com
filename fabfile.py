from __future__ import with_statement
from fabric.api import *

code_dir = '/var/www/PurplePikachu.com'
github_url = 'https://github.com/PatelEvinsTodd/PurplePikachu.com'
venvwrapper_path = '/usr/local/bin/virtualenvwrapper.sh'
venv = 'purplepikachu'
venv_dir = '$WORKON_HOME/' + venv

def dev():
    env.hosts = ['pokemon.tannerevins.com']
    env.branch = 'development'

def prod():
    env.hosts = ['purplepikachu.com']
    env.branch = 'master'

def deploy():
    env.user = 'oak'
    with settings(warn_only=True):
        if run('test -d %s' % code_dir).failed:
            run('echo \'First deployment. Login to root to initialize.\'')
            return
    with cd(code_dir):
        run("git pull origin %s" % env.branch)

def initRepo():
    env.user = 'root'
    env.virtualenvsource = 'source %s' % venvwrapper_path
    env.activate = 'source %s/bin/activate' % venv_dir

    with settings(warn_only=True):
        if run('test -d %s' % code_dir).failed:
            if run('git clone %s %s' % (github_url, code_dir)).failed:
                run('echo \'Unable to clone repository.\'')
                return
            run('chown oak:oak -R %s' % code_dir)
        else:
            run('echo \'Repository already initialized.\'')
        if run('test -d %s' % venv_dir).failed:
            with prefix(env.virtualenvsource):
                run('mkvirtualenv %s' % venv)
                with prefix(env.activate):
                    run('pip install -r %s/requirements.txt' % code_dir)
