import os, argparse, time, stat, pwd, grp, glob
from tabulate import tabulate
from pwd import getpwuid
from stat import *

def get_files_list(filepath):
    files_list=[]
    if not args.a:
        for file in os.listdir(filepath) :
            if not file.startswith("."):
                files_list.append(file)
        return files_list
    else:
        return os.listdir(filepath)

def find_permission(stat_mode):
    mode=''
    mode_pattern={'0':'---','1':'--x','2':'-w-','3':'-wx','4':'r--','5':'r-x','6':'rw-','7':'rwx'}
    for digit in str(stat_mode):
        mode=mode+mode_pattern[digit]
    return mode

def find_owner(stat_uid):
    return pwd.getpwuid(stat_uid)[0]

def find_group(stat_gid):
    return grp.getgrgid(stat_gid)[0]

def find_file_type(filename, filepath):
    if os.path.isfile(filepath+'/'+filename):
        return '-'
    elif os.path.isdir(filepath+'/'+filename):
        return 'd'
    else:
        return '-'

def size_sort(long_format_list):
    size_sorted_list=sorted(long_format_list, key = lambda x:x[4])
    return size_sorted_list

def time_sort(long_format_list, index):
    time_sorted_list=sorted(long_format_list, key = lambda x:x[index]) 
    for entry in time_sorted_list:
        entry[index]=time.ctime(int(entry[index]))
    return time_sorted_list

def name_sort(long_format_list):
    name_sorted_list=sorted(long_format_list, key = lambda x:x[6])
    return name_sorted_list

def long_format(files_list, filepath):
    if args.R:
        print('\n{}:'.format(filepath))
    long_format_list=[]
    for filename in files_list:
        file_info=[]
        stat = os.stat(filepath+'/'+filename)
        stat_mode = oct(stat.st_mode)[-3:]
        file_type = find_file_type(filename, filepath)
        mode = find_permission(stat_mode)
        owner = find_owner(stat.st_uid)
        group = find_group(stat.st_gid)
         
        file_info.append("{}{}".format(file_type, mode))   
        file_info.append("{}".format(stat.st_nlink))
        file_info.append("{}".format(owner))
        file_info.append("{}".format(group))
        file_info.append(int(stat.st_size))
        if args.t:
            if args.u:
                file_info.append("{}".format(int(stat.st_atime)))
            elif args.U:
                file_info.append("{}".format(int(stat.st_ctime)))
            else:
                file_info.append("{}".format(int(stat.st_mtime)))
        elif not args.t:
            if args.u:
                file_info.append("{}".format(time.ctime(stat.st_atime)))
            elif args.U:
                file_info.append("{}".format(time.ctime(stat.st_ctime)))
            else:
                file_info.append("{}".format(time.ctime(stat.st_mtime)))
        file_info.append("{}".format(filename))
        long_format_list.append(file_info)
    if args.t:
        print_format(time_sort(long_format_list,5))
    elif args.s:
        print_format(size_sort(long_format_list))
    else:
        print_format(name_sort(long_format_list))
    if args.R:
        for file in files_list:
            if os.path.isdir(filepath+'/'+file):
                files_list=get_files_list(filepath+'/'+file)
                long_format(files_list,filepath+'/'+file)

def short_format(files_list, filepath):
    # print(files_list, filepath)
    if args.R and filepath != '.':
        print('{}:'.format(filepath))
    for file in files_list:
        print(file+"\t\t",end="")
    print("\n")
    if args.R:
        for file in files_list:
            # print("sample")
            if os.path.isdir(filepath+'/'+file):
                files_list=get_files_list(filepath+'/'+file)
                short_format(files_list,filepath+'/'+file)


def list_directory(filepath):
    if (not args.l and not args.s and not args.t and not args.u and not args.U):
        files_list=get_files_list(filepath)
        short_format(files_list, filepath)
        # for file in files_list:
        #     print(file+"\t",end="")
        # print("\n")
        # max_len=len(max(files_list, key=len))
        # print(max_len)
        # for file in files_list:
        #     print(file, end =" ")
        #     for i in range(max_len-len(file)):
        #         print(i)
        #         # print(" ",end =" ")


    if args.l or args.u or args.U:
        files_list=get_files_list(filepath)
        long_format(files_list, filepath)

def print_format(print_list):
    print(tabulate(print_list, tablefmt="plain"))

def main():
    if not len(args.file_path_list):
        list_directory(".")
    else:
        for filepath in args.file_path_list:
            if len(args.file_path_list)>1:
                print('\n{}:'.format(filepath))
            list_directory(filepath)
        
parser=argparse.ArgumentParser(description="For each operand that names a file of a type other than directory, list-directory displays its name as well as any requested, associated information. If no arguments are specified, by default list in long format")
parser.add_argument('-l', action='store_true', help='(The lowercase letter ``ell''.)  List in long format.')
parser.add_argument('-s', action='store_true', help='Sort files by size.')
parser.add_argument('-t', action='store_true', help='Sort by time modified.')
parser.add_argument('-u', action='store_true', help='Use time of last access, instead of last modification of the file for sorting (-t) or long printing (-l).')
parser.add_argument('-U', action='store_true', help='Use time of file creation, instead of last modification for sorting (-t) or long output (-l).')
parser.add_argument('-a', action='store_true', help='Include directory entries whose names begin with a dot \'.\'')
parser.add_argument('-R', action='store_true', help='Recursively list subdirectories encountered.')
parser.add_argument('file_path_list', type=str, nargs='*', help='list of file paths')

args=parser.parse_args()

if __name__ == "__main__":
    main()