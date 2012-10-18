#!/bin/sh

echo get local data...

cd %~dp0

%~d0

HOST=localhost
 
wget -O../android/res/raw/rooms.json --no-check-certificate http://$HOST:8082/default/rooms

wget -O../android/res/raw/sandbox.json --no-check-certificate http://$HOST:8082/default/sandbox
wget -O../android/res/raw/tracks.json --no-check-certificate http://$HOST:8082/default/tracks
wget -O../android/res/raw/sessions.json --no-check-certificate http://$HOST:8082/default/sessions
wget -O../android/res/raw/speakers.json --no-check-certificate http://$HOST:8082/default/speakers
wget -O../android/res/raw/common_slots.json --no-check-certificate http://$HOST:8082/default/commonslots


cp ../android/res/raw/sandbox.json /home/cr/develop/android/gdgsched/gae/src/templates/
cp ../android/res/raw/tracks.json /home/cr/develop/android/gdgsched/gae/src/templates/
cp ../android/res/raw/sessions.json /home/cr/develop/android/gdgsched/gae/src/templates/
cp ../android/res/raw/speakers.json /home/cr/develop/android/gdgsched/gae/src/templates/
cp ../android/res/raw/common_slots.json /home/cr/develop/android/gdgsched/gae/src/templates/



