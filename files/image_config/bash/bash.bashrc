# System-wide .bashrc file for interactive bash(1) shells.

# To enable the settings / commands in this file for login shells as well,
# this file has to be sourced in /etc/profile.

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, overwrite the one in /etc/profile)
PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '

# Commented out, don't overwrite xterm -T "title" -n "icontitle" by default.
# If this is an xterm set the title to user@host:dir
#case "$TERM" in
#xterm*|rxvt*)
#    PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME}: ${PWD}\007"'
#    ;;
#*)
#    ;;
#esac

# enable bash completion in interactive shells
if ! shopt -oq posix; then
    if [ -f /usr/share/bash-completion/bash_completion ]; then
      . /usr/share/bash-completion/bash_completion
    elif [ -f /etc/bash_completion ]; then
      . /etc/bash_completion
    fi
fi

# if the command-not-found package is installed, use it
if [ -x /usr/lib/command-not-found -o -x /usr/share/command-not-found/command-not-found ]; then
    function command_not_found_handle {
        # check because c-n-f could've been removed in the meantime
        if [ -x /usr/lib/command-not-found ]; then
            /usr/lib/command-not-found -- "$1"
            return $?
        elif [ -x /usr/share/command-not-found/command-not-found ]; then
           /usr/share/command-not-found/command-not-found -- "$1"
           return $?
        else
           printf "%s: command not found\n" "$1" >&2
           return 127
        fi
    }
fi

# enable auto-logout for console ttyS* sessions
tty | grep ttyS >/dev/null && TMOUT=300

# when the shell exits, append to the history file instead of overwriting it
shopt -s histappend

# saving 10000 lines to disk and loading the last 5000 lines into memory
export HISTSIZE=5000
export HISTFILESIZE=10000

# prompt_cmd was added to support logging the user commands with logger
# Get cmd num from history and verify it with previous cmd num
# to ignore duplicate logging due to <return> <ctrl+c> cases
prompt_cmd () {
    #Get last cmd from history
    lst_hist_cmd=$(history 1);
    #Get the first number/cmd_idx from last cmd
    read -a tmpnum <<<"${lst_hist_cmd//[^0-9]/ }"
    lst_hist_cmd_idx=${tmpnum[0]}
    exp_hist_cmd_idx=$((prv_lst_hist_cmd + 1))
    if [ "$exp_hist_cmd_idx" == "$lst_hist_cmd_idx" ]; then
        logger -p local5.debug "$(whoami) [$$]: $(echo $lst_hist_cmd | sed "s/^[ ]*[0-9]\+[ ]*//" )";
    fi
    #echo " Prv = $prv_lst_hist_cmd Lst = $lst_hist_cmd_idx "

    #Add additional commands that has to be executed as part of PROMPT_COMMAND below
    history -a; history -c; history -r;

    #For any change in cmd index due to append
    lst_hist_cmd=$(history 1);
    read -a tmpnum <<<"${lst_hist_cmd//[^0-9]/ }"
    lst_hist_cmd_idx=${tmpnum[0]}
    #echo "Append Prv = $prv_lst_hist_cmd Lst = $lst_hist_cmd_idx "
    prv_lst_hist_cmd=$lst_hist_cmd_idx
}

# after each command,log the command and append to the history file and reload
export PROMPT_COMMAND=prompt_cmd
