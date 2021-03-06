"""
perseuspy module for Python-Perseus interop.

Currently there is no support for the following Perseus matrix features:
 - numerical annotation rows
 - multi-numeric rows
"""

__version__ = '0.1.4'
try:
    import perseuspy.dependent_peptides
    import perseuspy.io
    from perseuspy.io.perseus import to_perseus, read_perseus
    # Monkey-patching pandas
    import pandas as pd
    pd.DataFrame.to_perseus = to_perseus
    pd.read_perseus = read_perseus
    from perseuspy.io.perseusNetwork import read_networks, write_networks
except ImportError as e: # this shold happen only during installation
    print(e)
