'''
Asterisk Manager API Python package.
'''

__author__ = 'David Wilson'
__id__ = '$Id$'

try:
    __revision__ = int('$Rev$'.split()[1])
except:
    __revision__ = None

__version__ = '0.1mfast'
__all__ = ['CLI', 'Config', 'Logging', 'Manager', 'Util']


cause_codes = {
    0: (0, 'UNKNOWN',        'Unkown'),
    1: (1, 'UNALLOCATED',    'Unallocated number'),
    16: (16, 'CLEAR',          'Normal call clearing'),
    17: (17, 'BUSY',           'User busy'),
    18: (18, 'NOUSER',         'No user responding'),
    21: (21, 'REJECTED',       'Call rejected'),
    22: (22, 'CHANGED',        'Number changed'),
    27: (27, 'DESTFAIL',       'Destination out of order'),
    28: (28, 'NETFAIL',        'Network out of order'),
    41: (41, 'TEMPFAIL',       'Temporary failure')
}

_AST_BANNERS = [
    'Asterisk Call Manager/1.0\r\n',
    'Asterisk Call Manager/1.1\r\n',
    'Asterisk Call Manager/1.2\r\n',
    'Asterisk Call Manager/1.3\r\n',
    'Asterisk Call Manager/2.5.0\r\n',
    'Asterisk Call Manager/2.6.0\r\n',
    'Asterisk Call Manager/2.7.0\r\n',
]


class BaseException(Exception):

    '''
    Base class for all py-Asterisk exceptions.
    '''

    _prefix = '(Base Exception)'
    _error = '(no error)'

    def __init__(self, error):
        self._error = error

    def __str__(self):
        return '%s: %s' % (self._prefix, self._error)
