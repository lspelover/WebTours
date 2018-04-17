import os
import sys

sys.path
print(sys.path)
print(os.path.split(os.path.split(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])[0])[0])
sys.path.append(os.path.split(os.path.split(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])[0])[0])
print(sys.path)
