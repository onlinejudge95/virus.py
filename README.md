virus.py
========

## Intro
This repo is the codebase for my proposed talk on
**Implemting a self replicating virus**.
Motivation behind this project is to understand how self replication works
using python and to see what are the possible impacts that can come out of it.


## Theory
According to wikipedia
> A computer virus is a type of computer program that, when executed, replicates itself by modifying other computer programs and inserting its own code.

What we are doing here is basically marking our script into a header section, nested within which is a payload section as described below.

### Header
This header marks the start and end of our entire replication logic.

### Payload
**PLEASE DO NOT TRY THIS AT YOUR HOME...........DIRECTORY**

This section contains a malicious code responsible for causing some disruption.
For educational purposes the repo contains only a print stetement, but in theory
you can try to attempt various activities including but not limited to.
1. Causing a fork bomb(though remember that a single instance of a fork bomb is enough to bring donw a system, but given the nature of this code, it will cause a massive threaded fork bomb {don't even know if that is a thing :p })
2. Causing a disk exhaustion by writing enormous amount of data to a file.
3. Add the machine in a botnet.

### Algorithm
```
1. Iterate over the lines of the current file.
2. Store all the lines between the `BEGIN HEADER` & `END HEADER` sections.
3. Iterate over all python files(recursively) in the given directory.
4. If the file contains the replication code do nothing
5. Else add the replication code to the file.
```

## TODOs
1. Obfuscate the code.