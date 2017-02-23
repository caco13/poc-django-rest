#! /bin/bash

# Usage info
show_help() {
    cat << EOF
    Usage: ${0##*/} [-h] [<file>]...
    Sends file objects to Django Rest Framework REST API witH httpie.
	Without list of files send all in current directory.
EOF
}

# Reset OPTIND in case getopts has been used previously in the shell.
OPTIND=1

while getopts "h?" opt; do
    case $opt in
		h)
			show_help
			exit 0
			;;
    esac
done

# Get all files in current directory and send them to REST API server
# Safe because we tested for h option
if [ $# -eq 0 ] ; then
	show_help >&2
	exit 1
else
	for file in $* ; do
		if ! [ -f $file ] ; then
			echo "Error: File $file does not exist."
			continue
		fi
		http -a indc:indc@indc -f POST http://127.0.0.1:8000/uploads/ datafile@"$file"
	done
fi

