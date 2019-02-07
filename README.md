# PythonSSG "Pumpkin Spice"
A command-line static-site generator written in Python.

## Project Details
This PythonSSG serves as semester-long project for CS 370: Software Engineering, oferred at SUNY Polytechnic Institute, Fall 2018. 

Authors: Christopher Scott, Jesse Lembo, Tim Rogers, Josh Rosenbaum

## Project Language/Libraries
Written in [Python](https://python.org) with [Markdown](https://github.com/Python-Markdown/markdown) framework for Python. Targeted as a desktop executable for command-line execution.

## Features
### Command Line Interface
- Create and manage projects.
- Build and regenerate static sites.
- Quick deployment.
### Markdown (.md) File Support
- Markdown to HTML conversion
- (Future possibility): Multimedia support.
### Speed
- The site atomically swaps updates without needing to be down (even for seconds).

## Usage Example
To view documentation on command-line, run pssg.py with no flags:
```
> pssg.py
  usage: pssg.py [-h] [-n NEWFILE] [-b BUILDFILE]
  optional arguments:
     -h, --help
     -n NEWFILE, --new NEWFILE
     -b BUILDFILE, --build BUILDFILE
```
