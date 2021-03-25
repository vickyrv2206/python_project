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
    
def get_files_list(filepath):
    if args.R:
        files_list=glob.glob(filepath+'/**',recursive = True)
        files_list.pop(0)
        [ files_list.append(file) for file in glob.glob(filepath+'/.*/**',recursive = True)]
    else:
        files_list=glob.glob(filepath+'/**')
        [ files_list.append(file) for file in glob.glob(filepath+'/.**')]
    # print(files_list)
    return files_list

def size_sort(long_format_list):
    size_sorted_list=sorted(long_format_list, key = lambda x:x[4])
    return size_sorted_list

def time_sort(long_format_list):
    time_sorted_list=sorted(long_format_list, key = lambda x:x[5])
    return time_sorted_list

def name_sort(long_format_list):
    name_sorted_list=sorted(long_format_list, key = lambda x:x[6])
    return name_sorted_list

def long_format(filepath):
    long_format_list=[]
    files_list=get_files_list(filepath)
    for filename in files_list:

        if filename.split('/')[-1].startswith(".") and not args.a:
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
        file_info.append(int(stat.st_size))
        file_info.append("{}".format(time.ctime(stat.st_mtime)))
        if args.f:
            file_info.append("{}".format(filename))
        else:
            # file_info.append("{}".format(filename.replace(filepath,"")))
            filename=filename.replace(filepath,"")
            if filename[0]=='/':
                filename=filename.replace('/',"")
            file_info.append("{}".format(filename))
        long_format_list.append(file_info)

    return name_sort(long_format_list)

def get_time(time_type, filepath):
    access_time_list=[]
    files_list=get_files_list(filepath)

    for filename in files_list:
        if filename.startswith(".") and not args.a:
            continue
        file_info=[]
        stat = os.stat(filename)
        if time_type == "access":
            file_info.append("{}".format(time.ctime(stat.st_atime)))
        elif time_type == "creation":
            file_info.append("{}".format(time.ctime(stat.st_ctime)))
        elif time_type == "both":
            file_info.append("{}".format(time.ctime(stat.st_atime)))
            file_info.append("{}".format(time.ctime(stat.st_ctime)))
        if args.f:
            file_info.append("{}".format(filename))
        else:
            filename=filename.replace(filepath,"")
            if filename[0]=='/':
                filename=filename.replace('/',"")
            file_info.append("{}".format(filename))
        access_time_list.append(file_info)
    return access_time_list

def tabular_display(display_list, header):
    print(tabulate(display_list, headers=header))

def list_files(filepath):
    long_header_list=["Mode","Links","Owner","Group","size","ModifiedTime","Filename"]
    
    if args.l or not args.u or not args.U:
        display_list=long_format(filepath)
        header=long_header_list
    
    if args.t:
        if args.s:
            pass
        elif not args.l:
            display_list=long_format(filepath)
        to_be_sorted=display_list
        display_list=time_sort(to_be_sorted)
        header=long_header_list
    
    if args.u and args.U:
        display_list=get_time("both", filepath)
        header=["AccessTime","CreationTime","Filename"]
    elif args.U:
        display_list=get_time("creation", filepath)
        header=["CreationTime","Filename"]
    elif args.u:
        display_list=get_time("access", filepath)
        header=["AccessTime","Filename"]

    if args.R or args.a or args.s:
        if args.u or args.U:
            pass
        elif not args.l:
            display_list=long_format(filepath)
            header=long_header_list
    
    if args.s and not args.u and not args.U:
        display_list=size_sort(display_list)
        header=long_header_list
    
    return display_list, header


def main():
    if not len(args.file_path_list):
        display_list=list_files(os. getcwd())
        # print(display_list)
        tabular_display(display_list[0],display_list[1])

    else:
        multiple_display_list=[]
        for filepath in args.file_path_list:
            display_list=list_files(filepath)
            [ multiple_display_list.append(entry) for entry in display_list[0] ]
        tabular_display(multiple_display_list,display_list[1])
        
parser=argparse.ArgumentParser(description="For each operand that names a file of a type other than directory, list-directory displays its name as well as any requested, associated information. If no arguments are specified, by default list in long format")
parser.add_argument('-l', action='store_true', help='(The lowercase letter ``ell''.)  List in long format.')
parser.add_argument('-s', action='store_true', help='Sort files by size.')
parser.add_argument('-t', action='store_true', help='Sort by time modified.')
parser.add_argument('-u', action='store_true', help='Use time of last access, instead of last modification of the file for sorting (-t) or long printing (-l).')
parser.add_argument('-U', action='store_true', help='Use time of file creation, instead of last modification for sorting (-t) or long output (-l).')
parser.add_argument('-a', action='store_true', help='Include directory entries whose names begin with a dot \'.\'')
parser.add_argument('-R', action='store_true', help='Recursively list subdirectories encountered.')
parser.add_argument('-f', action='store_true', help='Shows full file path')
parser.add_argument('file_path_list', type=str, nargs='*', help='list of file paths')

args=parser.parse_args()

if __name__ == "__main__":
    main()