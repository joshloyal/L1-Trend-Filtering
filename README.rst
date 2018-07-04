.. -*- mode: rst -*-

|Travis|_ |AppVeyor|_ |Coveralls|_ |CircleCI|_ |License|_

.. |Travis| image:: https://travis-ci.org/joshloyal/l1tf.svg?branch=master
.. _Travis: https://travis-ci.org/joshloyal/cookiecutter.project_slug}}

.. |AppVeyor| image:: https://ci.appveyor.com/api/projects/status/54j060q1ukol1wnu/branch/master?svg=true
.. _AppVeyor: https://ci.appveyor.com/project/joshloyal/l1tf/history

.. |Coveralls| image:: https://coveralls.io/repos/github/joshloyal/l1tf/badge.svg?branch=master
.. _Coveralls: https://coveralls.io/github/joshloyal/l1tf?branch=master

.. |CircleCI| image:: https://circleci.com/gh/joshloyal/l1tftree/master.svg?style=svg
.. _CircleCI: https://circleci.com/gh/joshloyal/l1tf/tree/master


.. |License| image:: https://img.shields.io/badge/License-GPL%20v2-blue.svg
.. _License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html


.. _scikit-learn: https://github.com/scikit-learn/scikit-learn

L1 Trend Filtering
=============================
This is a Python package wrapper around the C solver for the l1 trend filtering algorithm written by Kwangmoo Koh, Seung-Jean Kim and Stephen Boyd. It is compatible with scikit-learn_.


Documentation / Website: https://joshloyal.github.io/l1tf


Example
-------
Example that shows how to learn a one dimensional subspace from a dataset with ten features:

.. code-block:: python

    print("Hello, world!")

Installation
------------

Dependencies
------------
L1 Trend Filtering requires:

- Python (>= 2.7 or >= 3.4)
- NumPy (>= 1.8.2)
- SciPy (>= 0.13.3)
- Scikit-learn (>=0.17)

Additionally, to run examples, you need matplotlib(>=2.0.0).

Installation
------------
You need a working installation of numpy and scipy to install L1 Trend Filtering. If you have a working installation of numpy and scipy, the easiest way to install l1tf is using ``pip``::

    pip install -U l1tf

If you prefer, you can clone the repository and run the setup.py file. Use the following commands to get the copy from GitHub and install all the dependencies::

    git clone https://github.com/joshloyal/l1tf.git
    cd l1tf
    pip install .

Or install using pip and GitHub::

    pip install -U git+https://github.com/joshloyal/l1tf.git


Testing
-------
After installation, you can use pytest to run the test suite via setup.py::

    python setup.py test

References:
-----------
