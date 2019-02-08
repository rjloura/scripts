#
# Find where any available python module is located. 
#
# You could do:
#   pip list -v | grep <module>
#
# But that will only give you modules controled by pip, and the pip versions
# installed.
#
import os, sys

if len(sys.argv) is not 2:
    print("Usage: python<ver> wheres_my_module.py <module name>")
    exit(1)

mod_name = sys.argv[1]

found = False
for p in sys.path:
    print("Checking {}".format(p))
    try:
        os.stat(p)
    except OSError as e:
        print("{} doesnt exist, skipping\n".format(p))
        continue
           
    if mod_name in os.listdir(p):
        print("\n    Found {} in {}\n".format(mod_name, p))
        found = True

if not found:
    print("\nCould not find {}\n".format(mod_name))
