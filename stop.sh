#!/bin/bash
echo "Killed" > "/tmp/acdcaster.log"

kill -9 $(cat /tmp/acdcaster-server.pid)
kill -9 $(cat /tmp/acdcaster-abcde.pid)

rm /tmp/acdcaster-server.pid
rm /tmp/acdcaster-abcde.pid
rm /tmp/acdcaster.pid

killall "abcde"
killall "cdparanoia"
