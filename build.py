#!/bin/python3
import subprocess
import sys
import os

debug = False

p = subprocess.run(
    ["galac", "-o", "program", "main.gala"],
    capture_output=True,
    text=True
)

if p.stdout:
    print(p.stdout)
if p.stderr:
    print(p.stderr)

print("compiler returned", p.returncode)
if p.returncode != 0:
    sys.exit(p.returncode)

env = os.environ.copy()
env["LD_LIBRARY_PATH"] = ".:/"

def run():
    print("running.", flush=True)

    p = subprocess.Popen(
        ["stdbuf", "-oL", "./program"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        env=env,
    )

    for line in p.stdout:
        print(line, end="", flush=True)

    p.stdout.close()
    result = p.wait()

    print(f"\nprogram returned {result}")
    if result != 0:
        sys.exit(result)

def memcheck():
    p = subprocess.run(
        ["valgrind", "--leak-check=full", "./program"],
        capture_output=True,
        text=True,
    )

    if p.stdout:
        print(p.stdout)
    if p.stderr:
        print(p.stderr)

    print("memcheck returned", p.returncode)
    if p.returncode != 0:
        sys.exit(p.returncode)

try:
    run()
except KeyboardInterrupt:
    print("^C - canceling run.")
