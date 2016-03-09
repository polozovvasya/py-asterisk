#!/usr/bin/env python

'''
py-Asterisk distutils script.
'''

__author__ = 'David Wilson'
__id__ = '$Id$'

from distutils.core import setup


setup(
    name='py-Asterisk',
    version='0.5.3.1',
    description='Asterisk Manager API Python interface. Forked by Mikhail Fast',
    author='David Wilson',
    author_email='mouseratti@gmail.com',
    license='MIT',
    url='https://github.com/mouseratti/py-asterisk/',
    packages=['Asterisk'],
    scripts=['asterisk-dump', 'py-asterisk']
)
