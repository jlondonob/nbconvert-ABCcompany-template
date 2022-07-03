import os
import sys

from setuptools import setup
from setuptools.command.develop import develop

try:
    import jupyter_core.paths as jupyter_core_paths
except:
    jupyter_core_paths = None


pjoin = os.path.join

class DevelopCmd(develop):
    prefix_targets = [
        # prefix target and name of the template
        ("nbconvert/templates", 'ABCcompany')
    ]
    def run(self):
        # sys.prefix: environment path if active, else directory where python files installed
        target_dir = os.path.join(sys.prefix, 'share', 'jupyter')

        for prefix_target, name in self.prefix_targets:
            source = os.path.join('share', 'jupyter', prefix_target, name) # path to template in package
            target = os.path.join(target_dir, prefix_target, name)
            target_subdir = os.path.dirname(target)
            if not os.path.exists(target_subdir):
                os.makedirs(target_subdir)
            rel_source = os.path.relpath(os.path.abspath(source), os.path.abspath(target_subdir))
            try:
                os.remove(target)  # Delete template if already exists
            except:
                pass
            print(rel_source, '->', target)
            os.symlink(rel_source, target)

        super(DevelopCmd, self).run()


data_files = []
for root, dirs, files in os.walk('share'):
    root_files = [os.path.join(root, i) for i in files]
    data_files.append((root, root_files))

setup_args = {
    'name': 'nbconvert-ABCcompany',
    'version': '0.1.0',
    'packages': [],
    'data_files': data_files,
    'install_requires': [],
    'author':"José Londoño",
    'author_email': "jose@humanld.io",
    'url': 'https://github.com/HumanLD/nbconvert-ABCcompany-template',
    'options': {
        'bdist_wheel': {'universal':'1'}
        },
    'cmdclass': {
        'develop': DevelopCmd,
    } if jupyter_core_paths else {},
}

if __name__ == '__main__':
    setup(**setup_args)
