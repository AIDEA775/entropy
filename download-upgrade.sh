#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <user@target-remote-host>"
    echo "Download system update on remote pc"
    exit 1
fi

PKGLIST=`date "+pkglist-%y-%m"`
PKGDIR="$PKGLIST-download"
REMOTE=$1

echo "pkglist name: $PKGLIST"
echo "pkgdir name: $PKGDIR"
echo "remote pc: $REMOTE"
echo

echo "Update databases"
if ! sudo pacman -Sy; then
    exit 1
fi

echo
echo "Generate list of pkgs"
if ! sudo pacman -Sup --noconfirm > /tmp/$PKGLIST; then
    exit 1
fi

echo "Copy list to remote pc"
if ! scp $PKGLIST $REMOTE:; then
    exit 1
fi

read -n1 -p "Start download? [y/n] " doit
echo

if [[ "$doit" == "y" ]];
then
    ssh $REMOTE "mkdir -p $PKGDIR && wget -nv -P $PKGDIR -i $PKGLIST < /dev/null > $PKGLIST.log 2>&1 &"
    echo "Downloading..."
fi
echo "Done."
