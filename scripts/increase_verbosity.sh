#!/bin/sh
# Remember VERBOSE only works on debug builds of the app
adb shell setprop log.tag.gdgsched_SyncHelper VERBOSE
adb shell setprop log.tag.gdgsched_SessionsHandler VERBOSE

adb shell setprop log.tag.gdgsched_ScheduleProvider VERBOSE

adb shell setprop log.tag.gdgsched_GCM VERBOSE





adb shell setprop log.tag.gdgsched_ImageCache VERBOSE
adb shell setprop log.tag.gdgsched_ImageWorker VERBOSE
adb shell setprop log.tag.gdgsched_ImageFetcher VERBOSE