leet
====
    
.. image:: https://coveralls.io/repos/github/JaneTurueva/py-leet/badge.svg?branch=master
    :target: https://coveralls.io/github/JaneTurueva/py-leet?branch=master
    :alt: Coveralls

.. image:: https://travis-ci.org/JaneTurueva/py-leet.svg?branch=master
    :target: https://travis-ci.org/JaneTurueva/py-leet
    :alt: Travis CI

.. image:: https://img.shields.io/pypi/v/leet.svg
    :target: https://pypi.python.org/pypi/leet/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/wheel/leet.svg
    :target: https://pypi.python.org/pypi/leet/

.. image:: https://img.shields.io/pypi/pyversions/leet.svg
    :target: https://pypi.python.org/pypi/leet/

.. image:: https://img.shields.io/pypi/l/leet.svg
    :target: https://pypi.python.org/pypi/leet/


Command-line tool and library for `leeting text`_.

Library uses following vocabulary:
 
========  ===========
Original  Replacement
========  ===========
A a       @
E e       3
I i       1
O o       0
S s       5
========  ===========

Installation
------------

.. code-block:: shell

    pip install leet
    
    
Command-line usage
------------------
.. code-block:: shell

    leet Hello, world!
    > H3ll0, w0rld!


Library usage
-------------
.. code-block:: shell

    from leet import leet
    
    print(leet('Hello, world!'))


Performance
-----------

Is applicable for python 3.5+. Python 3.4 and lower would be slower.

==========  ==========  =======
Str length  Iterations  Time
==========  ==========  =======
512         1000        0.0071
64kb        1000        0.1458
1mb         100         0.1522
1mb         10          0.0154
10mb        2           0.0298
==========  ==========  =======


Versioning
==========

This software follows `Semantic Versioning`_

.. _leeting text: https://en.wikipedia.org/wiki/Leet
.. _Semantic Versioning: http://semver.org/
