#/bin/bash
_cryptkit()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="-v -p -n -i -g -c -h -u -l -e --version --price --into --gpu --convert --help --usage --list --exchanges"
    #opts="--help --verbose --version"

    if [[ ${cur} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi
}
complete -F _cryptkit cryptkit
