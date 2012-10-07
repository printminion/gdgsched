


import urllib2
import json



APP_NAME = "GDGDevFest-Android-App"
API_KEY = "AIzaSyCsAij0bSMlGHdta3snhfxD4rAOw9WeSDg" #from the APIs console
CLIENT_ID = "903246180582.apps.googleusercontent.com" #from the APIs console

    
#gdgdevfest

    
# Conference API - specific config
# NOTE: the backend used for the Google I / O 2012 Android app is not currently open source, so
# you should modify these fields to reflect your own backend.
CONFERENCE_API_KEY = "AIzaSyA2MhtOhocnrkFvc_uyavMbrLj_Qi36Vak"
ROOT_EVENT_ID = "devfest2012"
BASE_URL = "https://google-developers.appspot.com/_ah/api/resources/v0.1"
# BASE_URL = "https://kupriyanov7/_ah/api/resources/v0.1";
# BASE_URL = "https://kupriyanov7:8080/api";
BASE_URL = 'http://www.devfest.info'
#BASE_URL = 'http://localhost:8080'


GET_ALL_EVENTS_URL = BASE_URL + "/json/events?parent_event=" + ROOT_EVENT_ID + "&api_key=" + CONFERENCE_API_KEY
GET_EVENT_DATA_URL = BASE_URL + '/json/event/%s?parent_event=' + ROOT_EVENT_ID + '&api_key=' + CONFERENCE_API_KEY
GET_ALL_TRACKS_URL = BASE_URL + "/json/event/%s/tracks?parent_event=" + ROOT_EVENT_ID + "&api_key=" + CONFERENCE_API_KEY
GET_ALL_SESSIONS_URL = BASE_URL + "/json/event/%s/sessions?parent_event=" + ROOT_EVENT_ID + "&api_key=" + CONFERENCE_API_KEY
GET_ALL_SPEAKERS_URL = BASE_URL + "/json/event/%s/speakers?event_id=" + ROOT_EVENT_ID + "&api_key=" + CONFERENCE_API_KEY
GET_ALL_SPONSORS_URL = BASE_URL + "/json/event/%s/sponsors?event_id=" + ROOT_EVENT_ID + "&api_key=" + CONFERENCE_API_KEY

GET_ALL_ANNOUNCEMENTS_URL = BASE_URL + "/json/event/%s/announcements?parent_event=" + ROOT_EVENT_ID + "&api_key=" + CONFERENCE_API_KEY
EDIT_MY_SCHEDULE_URL = BASE_URL + "/editmyschedule/o/"

# Static file host for the sandbox data
GET_SANDBOX_URL = "https://developers.google.com/events/io/sandbox-data"
    
#
#('^/json/events$', JsonEventListPage),
#('^/json/event/(.*)$', JsonEventPage),
#('^/json/event/(.*)/tracks$', JsonTrackListPage),
#('^/json/event/(.*)/sessions$', JsonSessionListPage),
#('^/json/event/(.*)/speakers$', JsonSpeakerListPage),
#('^/json/event/(.*)/sponsors$', JsonSponsorListPage),

#http://www.devfest.info/ json / events



def validateEvents():
    
    req = urllib2.Request(GET_ALL_EVENTS_URL)
    response = urllib2.urlopen(req)
    the_page = response.read()
    
    events = json.loads(the_page)


#    print events
    
    for event in events:
        print 'city:%s' % event['city']
        validateEvent(event['event_id'])
        #break
    

def validateEvent(event_id):
    url = GET_EVENT_DATA_URL % event_id
    print 'validateEvent:%s' % url
    
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    
    #print the_page

    try:
        print 'tracks:%s' % validateTracks(event_id)
    except Exception as e:
        print e
    
    try:
        print 'sessions:%s' % validateSessions(event_id)
    except Exception as e:
        print e
    
    try:
        print 'speakers:%s' % validateSpeakers(event_id)
    except Exception as e:
        print e
    
    try:
        print 'sponsors:%s' % validateSponsors(event_id)
    except Exception as e:
        print e
 
def validateSessions(event_id):
    url = GET_ALL_SESSIONS_URL % event_id
    print 'validateSessions:%s' % url
    
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    
#    print the_page  
    sessions = json.loads(the_page)
    return len(sessions)  
    
 
def validateTracks(event_id):
    url = GET_ALL_TRACKS_URL % event_id
    print 'validateTracks:%s' % url
    
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    
#    print the_page   
    tracks = json.loads(the_page)
    return len(tracks) 

def validateSpeakers(event_id):
    url = GET_ALL_SPEAKERS_URL % event_id
    print 'validateSpeakers:%s' % url
    
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    
#    print the_page   
    tracks = json.loads(the_page)
    return len(tracks) 

def validateSponsors(event_id):
    url = GET_ALL_SPONSORS_URL % event_id
    print 'validateSponsors:%s' % url
    
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    
#    print the_page   
    tracks = json.loads(the_page)
    return len(tracks)

                         
validateEvents()
    
