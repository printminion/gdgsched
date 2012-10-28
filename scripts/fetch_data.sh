#!/bin/sh

echo get local data...

cd %~dp0

%~d0

HOST=localhost
PORT=8080

 
wget -O../android/res/raw/rooms.json --no-check-certificate http://$HOST:$PORT/default/rooms

wget -O../android/res/raw/sandbox.json --no-check-certificate http://$HOST:$PORT/default/sandbox
wget -O../android/res/raw/tracks.json --no-check-certificate http://$HOST:$PORT/default/tracks
wget -O../android/res/raw/sessions.json --no-check-certificate http://$HOST:$PORT/default/sessions
wget -O../android/res/raw/speakers.json --no-check-certificate http://$HOST:$PORT/default/speakers
wget -O../android/res/raw/common_slots.json --no-check-certificate http://$HOST:$PORT/default/commonslots


cp ../android/res/raw/sandbox.json /home/cr/develop/android/gdgsched/gae/src/templates/
cp ../android/res/raw/tracks.json /home/cr/develop/android/gdgsched/gae/src/templates/
cp ../android/res/raw/sessions.json /home/cr/develop/android/gdgsched/gae/src/templates/
cp ../android/res/raw/speakers.json /home/cr/develop/android/gdgsched/gae/src/templates/
cp ../android/res/raw/common_slots.json /home/cr/develop/android/gdgsched/gae/src/templates/



