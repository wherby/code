import sys,os
parent_directory_concise= os.path.dirname(os.path.abspath(__file__))
for i in range(2):
    parent_directory_concise = os.path.dirname(parent_directory_concise)
sys.path.append(parent_directory_concise)
print("init_setting and python path added...")