# # import os, argparse, time, stat
# # from tabulate import tabulate
# # from stat import *

# # def find_permission(stat_mode):
# #     mode = os.stat('README.md')
# #     if mode.S_IRUSR:
# #         print('got it')
# #     else:
# #         print('lose it')
# #     # mode=''
# #     # for i in range(9):
# #     #     print(i)
# #     #     # if S_IRUSR(stat_mode) or S_IRGRP(stat_mode) or S_IROTH(stat_mode):
# #     #     #     mode=mode+'r'
# #     #     # elif S_IWUSR(stat_mode) or S_IWGRP(stat_mode) or S_IWOTH(stat_mode):
# #     #     #     mode=mode+'w'
# #     #     # elif S_IXUSR(stat_mode) or S_IXGRP(stat_mode) or S_IXOTH(stat_mode):
# #     #     #     mode=mode+'x'
# #     #     # else:
# #     #     #     mode=mode+'-'
# #     # return mode

# # print(find_permission(33188))

# # mode=33188
# # print(S_IRUSR(mode))

# import os
# import stat

# def isgroupreadable(filepath):
#     st = os.stat(filepath)
#     # if (st.st_mode & ( stat.S_IRUSR or stat.S_IRGRP or stat.S_IROTH)) :
#     #     mode=mode+'r'
#     # elif: (st.st_mode & ( stat.S_IWUSR or stat.S_IWGRP or stat.S_IWOTH)) :
#     #     mode=mode+'w'
#     # elif: (st.st_mode & ( stat.S_IXUSR or stat.S_IXGRP or stat.S_IXOTH)) :
#     #     mode=mode+'x'
#     # else:
#     #     mode=mode+'-'
#     # sample=S_IRUSR
#     if (st.st_mode & (  stat. )):
#         print('True')




        

# print(isgroupreadable('README.md'))
# import ctypes
# import os

# def is_hidden(filepath):
#     name = os.path.basename(os.path.abspath(filepath))
#     return name.startswith('.') or has_hidden_attribute(filepath)

# def has_hidden_attribute(filepath):
#     try:
#         attrs = ctypes.windll.kernel32.GetFileAttributesW(unicode(filepath))
#         assert attrs != -1
#         result = bool(attrs & 2)
#     except (AttributeError, AssertionError):
#         result = False
#     return result


import os
from os.path import join, getsize
for root, dirs, files in os.walk('.'):
    print (root, "consumes",)
    print (sum(getsize(join(root, name)) for name in files),)
    print ("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS')
