## Generic
c.JupyterHub.admin_access = True
c.Spawner.default_url = '/lab'

## Authenticator
from jhub_cas_authenticator.cas_auth import CASAuthenticator
c.JupyterHub.authenticator_class = CASAuthenticator

# The CAS URLs to redirect (un)authenticated users to.
c.CASAuthenticator.cas_login_url = 'https://cas.uvsq.fr/login'
c.CASLocalAuthenticator.cas_logout_url = 'https://cas.uvsq/logout'

# The CAS endpoint for validating service tickets.
c.CASAuthenticator.cas_service_validate_url = 'https://cas.uvsq.fr/serviceValidate'

# The service URL the CAS server will redirect the browser back to on successful authentication.
c.CASAuthenticator.cas_service_url = 'https://%s/hub/login' % os.environ['HOST']

c.Authenticator.admin_users = { 'lucadefe' }


## Docker spawner
import os

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# Other stuff
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '10G'


## Services
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
