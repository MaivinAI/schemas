import re
from setuptools import setup
from subprocess import Popen, PIPE


def get_version():
    """
    Returns project version as string from 'git describe' command.
    """
    pipe = Popen('git describe --tags --always', stdout=PIPE, shell=True)
    version = str(pipe.communicate()[0].rstrip().decode("utf-8"))
    return str(re.sub(r'-g\w+', '', version)[1:])


setup(
    name='edgefirst-schemas',
    version=get_version(),
    description='Maivin EdgeFirst Schemas',
    author='Au-Zone Technologies',
    author_email='info@au-zone.com',
    license='AGPL-3.0',
    url='https://maivin.edgefirst.ai',
    packages=[ 'edgefirst.schemas' ],
    install_requires=[ 'pycdr2' ],
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    setup_requires=['wheel'],
)
