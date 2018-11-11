#!/bin/bash

SCRIPT=$(readlink -f "$0")

SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH

# rm -f .config
touch .config

echo "alias bahn=\"python $SCRIPTPATH/db_console/db_user_program.py\"" >> .config
echo "alias bahn_info=\"python $SCRIPTPATH/db_console/db_info.py\"" >> .config

echo "source $SCRIPTPATH/.config" >> $HOME/.bashrc
echo "source $SCRIPTPATH/.config" >> $HOME/.zshrc

source $SCRIPTPATH/.config

