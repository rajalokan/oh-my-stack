#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys


parser = argparse.ArgumentParser()
parser.add_argument("-a",
    "--actions",
    required=True,
    help="Space separated actions"
)
args = parser.parse_args()

def bootstrap(actions):
    for action in actions:
        file_path = os.path.join(".", "scripts", action + ".sh")
        subprocess.call(file_path, shell=True)

if __name__ == "__main__":
    bootstrap(args.actions.split(" "))
