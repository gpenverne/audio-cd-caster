#!/bin/bash
if [ -f "/tmp/acdcaster.pid" ]; then
    exit 0
fi
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ ! -f "$DIR/.abcde.conf" ]; then
    cp "$DIR/.abcde.conf.dist" "$DIR/.abcde.conf"
    echo "OUTPUTDIR=$DIR" >> "$DIR/.abcde.conf"
    echo "WAVOUTPUTDIR=$DIR" >> "$DIR/.abcde.conf"
fi
rm -rf $DIR/abcde*

abcde -1 -o wav -c $DIR/.abcde.conf &
echo $! > /tmp/acdcaster-abcde.pid

nodejs $DIR/server.js &
echo $! > /tmp/acdcaster-server.pid

echo "Started" > "/tmp/acdcaster.log"
