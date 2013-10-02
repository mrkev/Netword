import inspect
import timeit

from KCTests import *
from netword import *

def test_netword():
    s = 'A.B   C.D [E.F G].C '
    equals(  find_outside_groups("hello.world [.]", '.', '[]'),       5) 
    equals(  find_outside_groups("hello world [.]", '.', '[]'),      -1)

    equals(  split_string_at_indexes('hello', [0]),        ['ello'])
    equals(  split_string_at_indexes('hello.world', [5]),  ['hello', 'world'])

def test_speak():
    equals( parse_node('A("Hello", 24)'),       {'id': 'A', 'name':'Hello', 'size':'24'})
    equals( parse_node('A(24,     "Hello")'),   {'id': 'A', 'name':'Hello', 'size':'24'})
    equals( parse_node('A(24)'),                {'id': 'A', 'size':'24'})
    equals( parse_node('A("Hello")'),           {'id': 'A', 'name':'Hello'})

if __name__ == "__main__":
    test_speak()
    print 'All modules tested.'