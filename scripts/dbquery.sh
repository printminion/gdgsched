#!/bin/sh
if [[ -z $ADB ]]; then ADB=adb; fi
$ADB shell "echo '$*' | sqlite3 -header -column /data/data/de.gdg.devfest.ka/databases/schedule.db"