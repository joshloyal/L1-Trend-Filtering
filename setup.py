from __future__ import print_function

import os
import sys

from setuptools import setup, find_packages


HERE = os.path.dirname(os.path.abspath(__file__))

# import ``__version__` from code base
exec(open(os.path.join(HERE, 'l1tf', 'version.py')).read())


with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]


with open('test_requirements.txt') as f:
    TEST_REQUIRES = [l.strip() for l in f.readlines() if l]


try:
    import numpy
except ImportError:
    print('numpy is required during installation')
    sys.exit(1)


try:
    import scipy
except ImportError:
    print('scipy is required during installation')
    sys.exit(1)


DISTNAME = 'L1 Trend Filtering'
DESCRIPTION = 'This is a Python package wrapper around the C solver for the l1 trend filtering algorithm written by Kwangmoo Koh, Seung-Jean Kim and Stephen Boyd.'
with open('README.rst') as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = 'Joshua D. Loyal'
MAINTAINER_EMAIL = 'jloyal25@gmail.com'
URL = 'https://joshloyal.github.io/l1tf'
DOWNLOAD_URL = 'https://pypi.org/project/l1tf/#files'
LICENSE = 'GPLv2'
VERSION = __version__
CLASSIFIERS = []


setup(
    name=DISTNAME,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    long_description=LONG_DESCRIPTION,
    zip_safe=False,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    extras_require={'test': TEST_REQUIRES},
    setup_requires=['pytest-runner'],
    tests_require=TEST_REQUIRES,
)
