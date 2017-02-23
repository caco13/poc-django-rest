#! /bin/bash

# TODO: retirar opção "d". Enviar número de objetos default sem opção

# Usage info
show_help() {
   cat << EOF
   Usage: ${0##*/} [-h] [-d] [-n n]
   Envia objetos texto, criados automaticamente, ou objetos arquivo para
   a API REST Django Rest Framework.

        -h              mostra essa ajuda e sai
        -d              envia 10 objetos texto
        -n n            Envia n objetos texto
EOF
}

##
# Print a Lorem Ipsum sentence with Perl
li_sentence() {
    perl -e 'use Text::Lorem; my $text = Text::Lorem->new(); print $text ->sentences(1);'
}

##
# Print a Lorem Ipsum paragraph with Perl
li_paragraph() {
    perl -e 'use Text::Lorem; my $text = Text::Lorem->new(); print $text->paragraphs(1);'
}

##
# Genereates Lorem Ipsum fields values and send them through API
send_li_objects() {
    for ((i=0; i < $1; i++)) do
        title=$(li_sentence)
        description=$(li_paragraph)
        declare -i nes_id=$i+1

        # Requires user and password created in API
        # Change indc:indc@indc with <user>:<password> in your system
        # Change 10.0.2.2:8000 with <ip>:<port> of your API server
        http -a indc:indc@indc http://10.0.2.2:8000/experiments/ title="$title" description="$description" nes_id=$nes_id
    done
}

# Reset OPTIND in case getopts has been used previously in the shell.
OPTIND=1

##
# Constants
readonly DEFAULT_NUM_OBJECTS=10
readonly MIN_OBJECTS=1
readonly MAX_OBJECTS=100

while getopts "h?dn:" opt; do
    case $opt in
        h)
            show_help
            exit 0
            ;;
        d)

            # Generate Lorem Ipsums texts to variables and send objects to server
            send_li_objects DEFAULT_NUM_OBJECTS
            ;;
        n)
            num=$OPTARG
            re='^[0-9]+$'
            # Tests if num is a not decimal number
            if ! [[ $num =~ $re ]] ; then
                echo "Option -n requires numeric argument"
                exit 1
            fi
            # We will limit number of objects that can be created in API
            if [[ $num -lt $MIN_OBJECTS || $num -gt $MAX_OBJECTS ]] ; then 
                echo $num
                echo "Option -n accepts a number between 1 and 100"
                exit 1
            fi

            # Generate Lorem Ipsums texts to variables and send objects to server
            send_li_objects $num 
            ;;
        *)
            show_help >&2
            exit 1
            ;;
    esac
done

