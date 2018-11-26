#source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
#source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
setopt SHARE_HISTORY
setopt HIST_IGNORE_ALL_DUPS
setopt auto_cd
setopt completealiases
autoload -U colors && colors
export MAKEFLAGS="-j9 -l8"
#export MAKEFLAGS="-j5 -l4"

PROMPT="%B[%F{magenta}%n%F{yellow}@%F{cyan}%M %F{white}%~]%F{green}$ %f%b"

typeset -U path
path=(~/bin $path[@])

HISTFILE=~/.history
HISTSIZE=10000
SAVEHIST=5000

# don't add garbage to history
function hist() {
    [[ "$#1" -lt 7 \
    || "$1" = "run-help "* \
    || "$1" = "cd "* \
    || "$1" = "man "* \
    || "$1" = "h "* \
    || "$1" = "~ "* ]]
    return $(( 1 - $? ))
}

zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'

autoload -Uz compinit
compinit
REPORTTIME=15

# key bindings
bindkey "\e[H" beginning-of-line
bindkey "\e[F" end-of-line
bindkey "\e[3~" delete-char
bindkey '^[[A' up-line-or-search
bindkey '^[[B' down-line-or-search
bindkey -v
