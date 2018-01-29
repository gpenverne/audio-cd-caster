#!/bin/bash

if [ ! -f "/tmp/acdcaster.pid" ]; then
    exit 0
fi

echo "Killed" > "/tmp/acdcaster.log"

kill -9 $(cat /tmp/acdcaster-server.pid)
kill -9 $(cat /tmp/acdcaster-abcde.pid)

rm /tmp/acdcaster-server.pid
rm /tmp/acdcaster-abcde.pid
rm /tmp/acdcaster-play-cd.pid
