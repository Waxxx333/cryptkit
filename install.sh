#!/bin/bash
script=("cryptkit.py")
cleaned=("$(echo ${script} | cut -d'.' -f1)")
RD=("\033[01;38;5;9m")
PNK=("\033[01;38;5;13m")
PRP=("\033[01;38;5;55m")
GRN=("\033[01;38;5;10m")
DRK=("\033[01;38;5;242m")
WHT=("\033[01;38;5;15m")
YLW=("\033[01;38;5;220m")
user=(${USER})
Version=(0.4)
shell=$(basename $SHELL)
echo -e "${DRK}Getting ready to install ${GRN}${script}"
echo -e "${DRK}Making ${GRN}${script} ${DRK}executable"
chmod +x ${script}
echo -e "${GRN}┏━┓${DRK}┳━┓${DRK}┓ ┳${DRK}┳━┓${DRK}┏┓┓${DRK}┳┏ ${PNK}o${DRK}┏┓┓"
echo -e "${GRN}┃  ${DRK}┃┳┛${DRK}┗┏┛${DRK}┃━┛ ${DRK}┃ ${DRK}┣┻┓${DRK}┃ ${DRK}┃ "
echo -e "${GRN}┗━┛${RD}┇${DRK}┗┛ ${RD}┇ ${RD}┇ ${YLW}₿ ${RD}┇ ${RD}┇${DRK} ┛${RD}┇ ${RD}┇"

if grep -qi "arch" /etc/os-release 2>/dev/null; then
    export DISTRO="Arch" 
elif grep -qi "debian" /etc/os-release 2>/dev/null; then
    export DISTRO="Debian" 
elif grep -qi 'fedora' /etc/os-release 2>/dev/null; then
    export DISTRO="Fedora" 
elif grep -qi "opensuse" /etc/os-release 2>/dev/null; then
    export DISTRO="openSUSE" 
elif [[ -d /data/data/com.termux ]]; then
    export DISTRO='Termux'
fi

install_script() {
    if [[ ${shell} == 'zsh' && -d /usr/share/zsh/functions/Completion/Linux/ ]] || [[ ${shell} == 'bash' && -d /usr/share/bash-completion/completions/ ]] || [[ ${shell} == 'bash' && -d /data/data/com.termux/files/usr/share/bash-completion ]]; then
    echo -e "${DRK}[${GRN}+${DRK}] ${GRN}Shell for ${PNK}${user} ${GRN}detected${PNK}:: ${GRN}${shell} ${DRK}[${GRN}+${DRK}]"
    echo -e "${GRN}Would you like to install a tab completion script for ${PNK}${cleaned} ?"
    read -p "[y/n]::$ " choice
        if [[ ${choice} == [yY] || ${choice} == [yY][eE][sS] ]]; then
            completion="True"
            if [[ ${shell} == 'zsh' ]]; then
                completion_script=./completion/cryptkit.zsh
            elif [[ ${shell} == 'bash' ]]; then
                completion_script=./completion/cryptkit.bash
            fi
        fi
    else
        echo -e "${RD}[!] ${GRN}${cleaned} ${RD}has tab completion but it looks like you don't have tab completion installed ${DRK}[${RD}!${DRK}]"
        echo -e "${GRN}You can manually install completion for ${PNK}${shell} ${GRN}and then rerun this installation script"
    fi
	echo -e "${DRK}Attempting to install ${GRN}${script} ${DRK}locally for ${GRN}${user}"
    if [[ -d $HOME/.local/bin/ ]]; then
        echo -e "${GRN}Copying ${PNK}${script} ${GRN}to ${PNK}$HOME/.local/bin/${cleaned}"
        cp ${script} $HOME/.local/bin/cryptkit
        if [[ ${completion} == 'True' ]]; then
            if [[ ${shell} == 'zsh' ]]; then
                echo -e "${GRN}Copying ${PNK}${completion_script} ${GRN}to ${PNK}/usr/share/zsh/functions/Completion/Linux/"
                sudo cp ${completion_script} /usr/share/zsh/functions/Completion/Linux/_cryptkit
            elif [[ ${shell} == 'bash' ]]; then
                echo -e "${GRN}Copying ${PNK}${completion_script} ${GRN}to ${PNK}/usr/share/bash-completion/completions/"
                sudo cp ${completion_script} /usr/share/bash-completion/completions/cryptkit
            fi
        fi
    elif [[ -d /data/data/com.termux/files/usr/bin && $(whoami) != 'root' ]]; then
        echo -e "${DRK}Termux and Termux user detected. ${GRN}Installing ${script} to ${PNK}/data/data/com.termux/files/usr/bin"
        cp ${script} /data/data/com.termux/files/usr/bin
        if [[ ${completion} == 'True' ]]; then
            echo -e "${GRN}Copying ${PNK}${completion_script} ${GRN}to\n ${PNK}/data/data/com.termux/files/usr/share/bash-completion/completions/"
            cp ${completion_script} /data/data/com.termux/files/usr/share/bash-completion/completions/cryptkit
        fi
    else
        echo -e "Copy file to /bin ? This will require your password."
        read -p ">>> " answer3
        if [[ ${answer3} == [yY] || ${answer3} == [yY][eE][sS] ]]; then
            chmod +x ${script}
            sudo cp ${script} /bin/cryptkit
            if [[ ${completion} == 'True' ]]; then
                if [[ ${shell} == 'zsh' ]]; then
                    echo -e "${GRN}Copying ${PNK}${completion_script} ${GRN}to ${PNK}/usr/share/zsh/functions/Completion/Linux/"
                    sudo cp ${completion_script} /usr/share/zsh/functions/Completion/Linux/_cryptkit
                elif [[ ${shell} == 'bash' ]]; then
                    echo -e "${GRN}Copying ${PNK}${completion_script} ${GRN}to ${PNK}/usr/share/bash-completion/completions/"
                    sudo cp ${completion_script} /usr/share/bash-completion/completions/cryptkit
                fi
            fi
        elif [[ ${answer3} == [nN] || ${answer3} == [nN][oO] ]]; then
            echo -e "${GRN}You can still run the script with${PNK}:\n./${GRN}${script} ${DRK}[${RD}-u${PNK}/${RD}--usage ${PNK}| ${RD}-c${PNK}/${RD}--card ${WHT}(${GRN}3060lhr ${PNK}| ${RD}580${WHT}) ${PNK}| ${RD}-l${PNK}/${RD}--list${DRK}]"
            echo -e "${RD}Or${PNK}:\n${GRN}python3 ${script} ${DRK}[${RD}-u${PNK}/${RD}--usage ${PNK}| ${RD}-c${PNK}/${RD}--card ${PNK}| ${RD}-l${PNK}/${RD}--list${DRK}]"
        fi
    fi
}
get_requests() {
    if [[ ${DISTRO} == "Arch" ]]; then
        echo -e "${GRN}Arch${PNK}-${GRN}based ${DRK}distro detected ${PNK}:: ${DRK}Installing ${GRN}python${PNK}-${GRN}pip"
        sudo pacman --noconfirm -S python-requests
        command python3 -c "import requests;" &>/dev/null
        if [[ $? == 0 ]]; then
            install_script
        else
            echo -e "${RD}You're going to have to manually install requests."
        fi
    elif [[ ${DISTRO} == "Debian" ]]; then
        echo -e "${GRN}Debian${PNK}-${GRN}based ${DRK}distro detected ${PNK}:: ${DRK}Installing ${GRN}python3${PNK}-${GRN}pip"
        sudo apt-get -y install python3-requests
        command python3 -c "import requests;" &>/dev/null
        if [[ $? == 0 ]]; then
            install_script
        else
            echo -e "${RD}You're going to have to manually install requests."
        fi
    elif [[ ${DISTRO} == "Fedora" ]]; then
        echo -e "${GRN}Fedora${PNK}-${GRN}based ${DRK}distro detected ${PNK}:: ${DRK}Installing ${GRN}python3${PNK}-${GRN}pip"
        sudo dnf install  python3-requests
        command python3 -c "import requests;" &>/dev/null
        if [[ $? == 0 ]]; then
            install_script
        else
            echo -e "${RD}You're going to have to manually install requests."
        fi
    elif [[ ${DISTRO} == "Termux" ]]; then
        echo -e "${GRN}Termux${PNK}-${GRN}based ${DRK}OS detected ${PNK}:: ${DRK}Installing ${GRN}python3${PNK}-${GRN}pip"
        pkg install python3
        pip install requests
        command python3 -c "import requests;" &>/dev/null
        if [[ $? == 0 ]]; then
            install_script
        else
            echo -e "${RD}You're going to have to manually install requests."
        fi
    elif [[ ${DISTRO} == "openSUSE" ]]; then
        echo -e "${GRN}Fedora${PNK}-${GRN}based ${DRK}distro detected ${PNK}:: ${DRK}Installing ${GRN}python3${PNK}-${GRN}pip"
        sudo zypper install python3-requests
        command python3 -c "import requests;" &>/dev/null
        if [[ $? == 0 ]]; then
            install_script
        else
            echo -e "${RD}You're going to have to manually install requests."
        fi
    fi
}

initialize() {
    command python3 -c "import requests;" &>/dev/null
    if [[ $? == 0 ]]; then
        echo -e "${GRN}requests found ${PNK}. . . ${GRN}Continuing installation"
        install_script
    elif [[ $? != 0 ]]; then
        echo -e "${RD}requests not found. Install now to continue script installation ?"
        read -p ">>> " answer1
        if [[ ${answer1} == [yY] || ${answer1} == [yY][eE][sS] ]]; then
            echo -e "${GRN}Attempting to install requests"
            get_requests
        elif [[ ${answer1} == [nN] || ${answer1} == [nN][oO] ]]; then
            echo -e "${RD}Aborting"
        fi
    fi
}
initialize
