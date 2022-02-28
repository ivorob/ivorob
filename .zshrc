# Load prompt information
autoload -U promptinit && promptinit

# Load version control information
autoload -Uz vcs_info
precmd() { vcs_info }

# Format the vcs_info_msg_0_ variable
zstyle ':vcs_info:git*' formats "%r/%b "

prompt adam2 grey

RPROMPT=\$vcs_info_msg_0_
