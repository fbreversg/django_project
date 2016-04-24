from fabric.api import local, lcd

def prepare_deployment():
    local('python manage.py test myapp')
    local('git add -p && git commit')

def deploy():
    with lcd('/Users/franciscobrevers/.virtualenvs/django_project/'):

        # With git...
        local('git pull')

        # With both
        local('python manage.py migrate myapp')
        local('python manage.py test myapp')
        local('sudo /Applications/MAMP/bin/apache2/bin/apachectl restart')
