import os
from importlib.machinery import SourceFileLoader

from setuptools import setup, find_packages


module_name = 'leet'

module = SourceFileLoader(
    module_name,
    os.path.join(module_name, '__init__.py')
).load_module()


setup(
    name='leet',
    version=module.__version__,
    author=module.__author__,
    author_email=module.__email__,
    license=module.__license__,
    description=module.__doc__,
    long_description=open("README.rst").read(),
    platforms="all",
    classifiers=[
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    entry_points={
      'console_scripts': [
          'leet = leet.main:main'
      ]
    },
    packages=find_packages(exclude=['tests']),
    extras_require={
        'develop': [
            'coverage!=4.3',
            'coveralls',
            'pylama',
            'pytest',
            'pytest-cov',
            'tox',
            'twine',
        ],
    },
    url='https://github.com/JaneTurueva/py-leet'
)
