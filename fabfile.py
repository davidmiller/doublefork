"""
Fab commands for doublefork
"""

from fabric.api import task, hosts, local, lcd,  cd, run
from fabric import operations

deadpan = 'happenup@deadpansincerity.com'

@task
def test():
    """
    Run our unittests
    """
    local('python -m pytest test')

@task
def make_docs():
    """
    Rebuild the documentation
    """
    with lcd('doc/'):
        local('make html')

@task
@hosts(deadpan)
def upload_docs():
    """
    Build, compress, upload and extract the latest docs
    """
    with lcd('doc/build/html'):
        local('rm -rf doubleforkdocs.tar.gz')
        local('tar zcvf doubleforkdocs.tar.gz *')
        operations.put('doubleforkdocs.tar.gz', '/home/happenup/webapps/doubleforkdocs/doubleforkdocs.tar.gz')
    with cd('/home/happenup/webapps/doubleforkdocs/'):
        run('tar zxvf doubleforkdocs.tar.gz')
