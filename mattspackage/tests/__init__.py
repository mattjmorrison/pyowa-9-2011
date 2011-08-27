from pkg_resources import load_entry_point

from os import path
import sys

sys.argv[1] = path.abspath(path.join(path.dirname(path.abspath(__file__)), 'features'))
load_entry_point('lettuce', 'console_scripts', 'lettuce')()

