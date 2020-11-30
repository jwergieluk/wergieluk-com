#!/bin/bash
 
set -e; set -u

CONFIG_DIR=`pwd`

link() {
	NAME="${HOME}/.$1"
	if [ ! -e $NAME  ] ; then
		CMD="ln -s ${CONFIG_DIR}/$1 ${HOME}/.$1"
		echo $CMD; 
		$CMD
	else
		echo "$1 already linked."
	fi
}


link vimrc

