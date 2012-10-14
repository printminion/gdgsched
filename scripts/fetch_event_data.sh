#!/bin/sh

echo get date from devfest.info data...

cd %~dp0

%~d0


#event id for vienna
#http://www.devfest.info/event/ag9zfmRldmZlc3RnbG9iYWxyDQsSBUV2ZW50GK2cAQw

EVENT_ID=ag9zfmRldmZlc3RnbG9iYWxyDQsSBUV2ZW50GK2cAQw


#api calls data
wget -O../android/res/raw/tracks.json --no-check-certificate http://www.devfest.info/json/event/$EVENT_ID/tracks
wget -O../android/res/raw/sessions.json --no-check-certificate http://www.devfest.info/json/event/$EVENT_ID/sessions
wget -O../android/res/raw/speakers.json --no-check-certificate http://www.devfest.info/json/event/$EVENT_ID/speakers

 
#static data
wget -O../android/res/raw/rooms.json --no-check-certificate http://www.devfest.info/json/event/$EVENT_ID/rooms
wget -O../android/res/raw/common_slots.json --no-check-certificate http://www.devfest.info/json/event/$EVENT_ID/commonslots


wget -O../android/res/raw/sandbox.json --no-check-certificate http://www.devfest.info/json/event/$EVENT_ID/sandbox



#copy all to 
cp ../android/res/raw/sandbox.json /home/cr/develop/android/gdgsched/gae/src/templates/
cp ../android/res/raw/tracks.json /home/cr/develop/android/gdgsched/gae/src/templates/
cp ../android/res/raw/sessions.json /home/cr/develop/android/gdgsched/gae/src/templates/
cp ../android/res/raw/speakers.json /home/cr/develop/android/gdgsched/gae/src/templates/
cp ../android/res/raw/common_slots.json /home/cr/develop/android/gdgsched/gae/src/templates/



