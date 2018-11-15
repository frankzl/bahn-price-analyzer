#!/bin/bash

INPM=$(command -v npm)
IPIP=$(command -v pip)
IPIP3=$(command -v pip3)

if [ -z "$IPIP" ];
then
    echo "okay.. you dont have pip huh.. we can still do this.."
    if [ -z "$IPIP3" ];
    then
        echo "okay i give up, you also dont have pip3.. its over"
        exit 1
    fi
fi
if [ -z "$INPM" ];
then
    echo "dude, you need to install npm first .."
    exit 1
fi


SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

echo $SCRIPTPATH

rm -f .config
touch .config

echo "alias bahn=\"python $SCRIPTPATH/db_console/db_user_program.py\"" >> .config
echo "alias bahn_info=\"python $SCRIPTPATH/db_console/db_info.py\"" >> .config

echo "source $SCRIPTPATH/.config" >> $HOME/.bashrc
echo "source $SCRIPTPATH/.config" >> $HOME/.zshrc

source $SCRIPTPATH/.config

npm install

pip install -r db_console/requirements.txt
