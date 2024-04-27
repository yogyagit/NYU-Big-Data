Python 3.10.8 (v3.10.8:aaaf517424, Oct 11 2022, 10:14:40) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/env python
... 
... def mapper(line):
...     tokens = line.strip().split("->")
...     for i in range(len(tokens) - 1):
...         for j in range(i + 1, len(tokens)):
...             print("{}->{}\t1".format(tokens[i], tokens[j]))
...             print("{}->{}\t0".format(tokens[j], tokens[i]))
... 
... 
... if __name__ == "__main__":
...     import sys
...     for line in sys.stdin:
