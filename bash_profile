rbenv init -
PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"
PATH="/usr/local/go/bin:${PATH}"
export PATH

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="/Users/ray/.sdkman"
[[ -s "/Users/ray/.sdkman/bin/sdkman-init.sh" ]] && source "/Users/ray/.sdkman/bin/sdkman-init.sh"
eval "$(rbenv init -)"

