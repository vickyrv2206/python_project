import os, argparse, time, stat, pwd, grp, glob
from tabulate import tabulate
from pwd import getpwuid
from stat import *

def find_permission(stat_mode):
    mode=''
    mode_pattern={'1':'--x','2':'-w-','3':'-wx','4':'r--','5':'r-x','6':'rw-','7':'rwx'}
    for digit in str(stat_mode):
        mode=mode+mode_pattern[digit]
    return mode

def find_owner(stat_uid):
    return pwd.getpwuid(stat_uid)[0]

def find_group(stat_gid):
    return grp.getgrgid(stat_gid)[0]

def get_file_type(filename):
    if os.path.isfile(filename):
        return '-'
    elif os.path.isdir(filename):
        return 'd'

def size_sort(long_format_list):
    size_sorted_list=sorted(long_format_list, key = lambda x:x[2])
    return size_sorted_list

def time_sort(long_format_list):
    time_sorted_list=sorted(long_format_list, key = lambda x:x[5])
    return time_sorted_list

def long_format():
    long_format_list=[]
    if args.R:
        files_list=glob.glob('**',recursive = True)
    else:
        files_list=os.listdir()
    for filename in files_list:
        if filename.startswith(".") and not args.a:
            continue
        
        file_info=[]

        stat = os.stat(filename)
        stat_mode = oct(stat.st_mode)[-3:]
        file_type = get_file_type(filename)
        mode = find_permission(stat_mode)
        owner = find_owner(stat.st_uid)
        group = find_group(stat.st_gid)
        
        file_info.append("{}{}".format(file_type, mode))   
        file_info.append("{}".format(stat.st_nlink))
        file_info.append("{}".format(owner))
        file_info.append("{}".format(group))
        file_info.append("{}".format(stat.st_size))
        file_info.append("{}".format(time.ctime(stat.st_mtime)))
        file_info.append("{}".format(filename))
        long_format_list.append(file_info)

    return long_format_list

def get_time(time_type):
    access_time_list=[]
    files_list=os.listdir()
    for filename in files_list:
        file_info=[]
        stat = os.stat(filename)
        if time_type == "access":
            file_info.append("{}".format(time.ctime(stat.st_atime)))
        elif time_type == "creation":
            file_info.append("{}".format(time.ctime(stat.st_ctime)))
        file_info.append("{}".format(filename))
        access_time_list.append(file_info)
    return access_time_list




def tabular_display(display_list, header):
    print(tabulate(display_list, headers=header))

parser=argparse.ArgumentParser(description="List file in directory from specified path")
parser.add_argument('-l', action='store_true', help='Displays files in long format')
parser.add_argument('-s', action='store_true', help='Sort files by size')
parser.add_argument('-t', action='store_true', help='Sort by time modified')
parser.add_argument('-u', action='store_true', help='Use time of last access')
parser.add_argument('-U', action='store_true', help='Use time of file creation')
parser.add_argument('-a', action='store_true', help='Include directory entries whose names begin with a dot \'.\'')
parser.add_argument('-R', action='store_true', help='Recursively search for files inside the current directory')

args=parser.parse_args()

def main():
    long_header_list=["Mode","Links","Owner","Group","size","ModifiedTime","Filename"]
    
    if args.l:
        display_list=long_format()
        header=long_header_list

    if args.s:
        if not args.l:
            display_list=long_format()
        to_be_sorted=display_list
        display_list=size_sort(to_be_sorted)
        header=long_header_list

    if args.t:
        if args.s:
            pass
        elif not args.l:
            display_list=long_format()
        to_be_sorted=display_list
        display_list=time_sort(to_be_sorted)
        header=long_header_list

    if args.u:
        display_list=get_time("access")
        header=["AccessTime","Filename"]

    if args.U:
        display_list=get_time("creation")
        header=["CreationTime","Filename"]
    
    if args.a:
        if not args.l:
            display_list=long_format()
            header=long_header_list

    if args.R:
        if not args.l:
            display_list=long_format()
            header=long_header_list

    tabular_display(display_list,header)


if __name__ == "__main__":
    main()