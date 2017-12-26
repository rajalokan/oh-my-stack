#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys

def main():
    # TODO: If git not installed, install it

    oms_path = os.path.join("/", "tmp", "oh-my-stack")
    if not os.path.exists(oms_path):
        subprocess.call("sudo apt -y install git", shell=True)
        subprocess.call("git clone https://github.com/rajalokan/oh-my-stack.git %s" % oms_path, shell=True)

    sys.path.insert(0, oms_path)
    os.chdir(oms_path)
    from bootstrap import bootstrap
    bootstrap(sys.argv[2].split(" "))

if __name__ == "__main__":
    main()
