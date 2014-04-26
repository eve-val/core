try: # pragma: no cover
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError: # pragma: no cover
    __import__('pkgutil').extend_path(__path__, __name__)

import os

def core_loadapp(config_name=None):
    from paste.deploy import loadapp
    if not config_name:
        if os.path.exists('local.ini'):
            config_name = 'config:local.ini'
        else:
            config_name = 'config:development.ini'
    here_dir = os.getcwd()
    loadapp(config_name, relative_to=here_dir)
