
# Pyls-smart list directory

  

Pyls-smart library allows you to get the name of the files inside particular folder and also some other informations based on the flags sent as command line arguments.

## Syntax
> pyls-smart [-h] [-l] [-s] [-t] [-u] [-U] [-a] [-R] [-r] [file_path_list [file_path_list ...]]

	positional arguments:
		file_path_list  list of file paths
	optional arguments:
		-h, --help  show this help message and exit
		-l  (The lowercase letter ``ell.) List in long format.
		-s  Sort files by size.
		-t  Sort by time modified.
		-u  Use time of last access, instead of last modification of thefile for sorting (-t) or long printing (-l).
		-U  Use time of file creation, instead of last modification for sorting (-t) or long output (-l).
		-a  Include directory entries whose names begin with a dot '.'
		-R  Recursively list subdirectories encountered.
		-r  sorts in reverse order

##  Usage

**Default behaviour**

By default the command gives the list of files inside the current directory

> $ pyls-smart

	CHANGELOG.txt  LICENCE.txt  MANIFEST.in  README.txt  dist  pyls-smart  pyls_smart.egg-info
	sample  sample.py  sample.txt  setup.cfg  setup.py  tests
  
  You can also pass a file path as an argument
  > $ pyls-smart /usr

	bin  standalone  libexec  sbin  local  lib  X11  X11R6  share

**Long format(-l)**

If you pass the -l flag along with the pyla-smart command it shows the file mode, owner of the file, group of the file, size of the file, modified time, filename under the current directory

  > $ pyls-smart -l

	drwxr-xr-x 4 coda staff 128 Thu Mar 25 23:04:55 2021 tests
	-rw-r--r-- 1 coda staff 680 Fri Mar 26 10:47:18 2021 setup.py
	-rw-r--r-- 1 coda staff 131 Fri Mar 26 09:50:35 2021 setup.cfg
	-rw-r--r-- 1 coda staff 128 Fri Mar 26 11:46:00 2021 sample.txt
	-rw-r--r-- 1 coda staff 171 Fri Mar 26 14:20:45 2021 sample.py
	drwxr-xr-x 4 coda staff 128 Thu Mar 25 23:13:33 2021 sample
	drwxr-xr-x 7 coda staff 224 Fri Mar 26 10:48:32 2021 pyls_smart.egg-info
	drwxr-xr-x 3 coda staff 96 Fri Mar 26 14:17:52 2021 pyls-smart
	drwxr-xr-x 5 coda staff 160 Fri Mar 26 10:48:32 2021 dist
	-rw-r--r-- 1 coda staff 304 Fri Mar 26 09:59:46 2021 README.txt
	-rw-r--r-- 1 coda staff 25 Fri Mar 26 07:32:22 2021 MANIFEST.in
	-rw-r--r-- 1 coda staff 1055 Fri Mar 26 07:34:12 2021 LICENCE.txt
	-rw-r--r-- 1 coda staff 274 Fri Mar 26 10:48:11 2021 CHANGELOG.txt

**Sort files by size (-s)**
This sorts the files list by size. Basically it sorts in ascending order. But you can override it by passing  **reverse(-r)** as additional argument to reverse the list.
> $ pyls-smart -l -s

	-rw-r--r--  1  coda  staff  25  Fri Mar 26 07:32:22 2021  MANIFEST.in
	drwxr-xr-x  3  coda  staff  96  Fri Mar 26 16:09:05 2021  pyls-smart
	drwxr-xr-x  4  coda  staff 128  Thu Mar 25 23:04:55 2021  tests
	drwxr-xr-x  4  coda  staff 128  Thu Mar 25 23:13:33 2021  sample
	-rw-r--r--  1  coda  staff 128  Fri Mar 26 11:46:00 2021  sample.txt
	-rw-r--r--  1  coda  staff 131  Fri Mar 26 09:50:35 2021  setup.cfg
	drwxr-xr-x  5  coda  staff 160  Fri Mar 26 10:48:32 2021  dist
	-rw-r--r--  1  coda  staff 171  Fri Mar 26 14:20:45 2021  sample.py
	drwxr-xr-x  7  coda  staff 224  Fri Mar 26 10:48:32 2021  pyls_smart.egg-info
	-rw-r--r--  1  coda  staff 274  Fri Mar 26 10:48:11 2021  CHANGELOG.txt
	-rw-r--r--  1  coda  staff 304  Fri Mar 26 09:59:46 2021  README.txt
	-rw-r--r--  1  coda  staff 680  Fri Mar 26 10:47:18 2021  setup.py
	-rw-r--r--  1  coda  staff  1055  Fri Mar 26 07:34:12 2021  LICENCE.txt
	-rw-r--r--  1  coda  staff  2161  Fri Mar 26 16:21:55 2021  README.md

**Sort files by time modified (-t)**
This sorts the files list by time modified. Basically it sorts in ascending order. But you can override it by passing  **reverse(-r)** as additional argument to reverse the list.
> $ pyls-smart -l -t

	drwxr-xr-x  4  coda  staff 128  Thu Mar 25 23:04:55 2021  tests
	drwxr-xr-x  4  coda  staff 128  Thu Mar 25 23:13:33 2021  sample
	-rw-r--r--  1  coda  staff  25  Fri Mar 26 07:32:22 2021  MANIFEST.in
	-rw-r--r--  1  coda  staff  1055  Fri Mar 26 07:34:12 2021  LICENCE.txt
	-rw-r--r--  1  coda  staff 131  Fri Mar 26 09:50:35 2021  setup.cfg
	-rw-r--r--  1  coda  staff 304  Fri Mar 26 09:59:46 2021  README.txt
	-rw-r--r--  1  coda  staff 680  Fri Mar 26 10:47:18 2021  setup.py
	-rw-r--r--  1  coda  staff 274  Fri Mar 26 10:48:11 2021  CHANGELOG.txt


**Shows use time of last access (-u)**
This shows the files list with use time of last access.
> $ pyls-smart -l -u
	
	-rw-r--r--  1  coda  staff 274  Fri Mar 26 10:48:12 2021  CHANGELOG.txt
	-rw-r--r--  1  coda  staff  1055  Fri Mar 26 10:16:44 2021  LICENCE.txt
	-rw-r--r--  1  coda  staff  25  Fri Mar 26 10:16:44 2021  MANIFEST.in
	-rw-r--r--  1  coda  staff  2161  Fri Mar 26 16:21:57 2021  README.md
	-rw-r--r--  1  coda  staff 304  Fri Mar 26 10:16:44 2021  README.txt
	drwxr-xr-x  5  coda  staff 160  Fri Mar 26 10:54:38 2021  dist
	drwxr-xr-x  3  coda  staff  96  Fri Mar 26 16:09:11 2021  pyls-smart

**Shows use time of file creation (-U)**
This shows the files list with use time of file creation.
> $ pyls-smart -l -U

	-rw-r--r--  1  coda  staff 274  Fri Mar 26 10:48:11 2021  CHANGELOG.txt
	-rw-r--r--  1  coda  staff  1055  Fri Mar 26 07:34:12 2021  LICENCE.txt
	-rw-r--r--  1  coda  staff  25  Fri Mar 26 07:32:22 2021  MANIFEST.in
	-rw-r--r--  1  coda  staff  2161  Fri Mar 26 16:21:55 2021  README.md
	-rw-r--r--  1  coda  staff 304  Fri Mar 26 09:59:46 2021  README.txt
	drwxr-xr-x  5  coda  staff 160  Fri Mar 26 10:48:32 2021  dist
	drwxr-xr-x  3  coda  staff  96  Fri Mar 26 16:09:05 2021  pyls-smart

**Shows hidden files (-a)**
Includes directory or file entries whose names begin with a dot '.'
> $ pyls-smart -l -a

	-rw-r--r-- 1  coda  staff  8196  Fri Mar 26 12:37:44 2021  .DS_Store
	drwxr-xr-x  13  coda  staff 416  Fri Mar 26 10:16:44 2021  .git
	-rw-r--r-- 1  coda  staff  26  Fri Mar 26 10:16:04 2021  .gitignore
	-rw-r--r-- 1  coda  staff 274  Fri Mar 26 10:48:11 2021  CHANGELOG.txt
	-rw-r--r-- 1  coda  staff  1055  Fri Mar 26 07:34:12 2021  LICENCE.txt
	-rw-r--r-- 1  coda  staff  25  Fri Mar 26 07:32:22 2021  MANIFEST.in

**Recursive search (-R)**
This list files recursively from the given path.
> $ pyls-smart -R

	./pyls_smart.egg-info:
	PKG-INFO  SOURCES.txt  entry_points.txt  top_level.txt  dependency_links.txt

	./sample:
	file.txt  one

	./sample/one:
	one.txt

**Reverse list (-r)**
This list files in reverse order/
> $ pyls-smart -r

	tests  setup.py  setup.cfg  sample.txt  sample.py  sample  pyls_smart.egg-info  pyls-smart  
	dist  README.txt  README.md  MANIFEST.in  LICENCE.txt  CHANGELOG.txt