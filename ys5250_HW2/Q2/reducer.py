Python 3.10.8 (v3.10.8:aaaf517424, Oct 11 2022, 10:14:40) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/env python
... 
... import sys
... 
... def reducer():
...     current_pair = None
...     current_count = 0
...     current_reverse_count = 0
...     
...     for line in sys.stdin:
...         pair, count = line.strip().split("\t")
...         count = int(count)
...         
...         if current_pair and current_pair != pair:
...             if current_count > 0 and current_reverse_count == 0:
...                 print("{}".format(current_pair))
...             current_count = 0
...             current_reverse_count = 0
...         
...         if count == 1:
...             current_count += 1
...         else:
...             current_reverse_count += 1
...         
...         current_pair = pair
... 
...     if current_pair and current_count > 0 and current_reverse_count == 0:
...         print("{}".format(current_pair))
... 
... if __name__ == "__main__":
...     reducer()
