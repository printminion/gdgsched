# -*- coding: utf-8 -*-
import os
import webapp2
import jinja2
import logging
import json
import urllib2
#from com.kupriyanov.spreadsheet.GoogleSpreadsheetParser import getRowValue
import time  
from settings import APP_SECRET
from settings import APP_ID
import hmac
import hashlib
import base64
import zlib
from google.appengine.api import users

EVENT_KEY = '0Akgh73WhU1qHdFRWUnEyNVpvSEliVEFnY3hxck0wcWc'


template_dir = os.path.join(os.path.dirname(__file__), 'templates/' + APP_ID)
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir)
                               , autoescape = True)



def getRowValue(row, format, column_name):
    logging.info('getRowValue[%s]:%s' % (column_name, row))
    
    if str(column_name) == '':
        raise ValueError('column_name must not empty')
        
    begin = row.find('%s:' % column_name)
    
    logging.info('begin:%s' % begin)
       
    if begin == -1:
        return ''
    
    begin = begin + len(column_name) + 1
    
       
    end = -1
    found_begin = False
    
    for entity in format:
        logging.info('checking:%s' % entity)
        
        if found_begin and row.find(entity) != -1:
            end = row.find(entity)
            break
        
        if entity == column_name:
            found_begin = True
    
    
    #check if last element
    if format[len(format) -1 ] == column_name:
        end = len(row)
    else:
        if end == -1:
            end = len(row)
        else:
            end = end - 2
        
    logging.info('%s:%s' % (column_name, row) )
    #logging.info('speakertitle[%s]' % speaker_title )
    #logging.info('%s:%s' % (column_name, row.find(column_name)))
#        logging.info('%s - %s' % (begin, end))
    
    value = row[begin: end].strip()
    
    logging.info('%s[%s-%s]:[%s]' % (column_name, begin, end, value))
    

    return value


class Handler(webapp2.RedirectHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
    @staticmethod
    def CreateEtag(data):
        """Returns string of hash of file content, unique per URL."""
        data_crc = zlib.crc32(data)
        return base64.b64encode(str(data_crc))
    
        
class MainPage(Handler):
    def render_front(self):
        self.render("index.html")
        
    def get(self):
        logging.info('get:')
        self.render_front()
    
    def post(self):
        logging.info('post:')
        self.render_front()
    
#    from google.appengine.api import oauth
#
## ...
#        try:
#            # Get the db.User that represents the user on whose behalf the
#            # consumer is making this request.
#            user = oauth.get_current_user()
#
#        except oauth.OAuthRequestError, e:
#            # The request was not a valid OAuth request.
#            # ...
_event = 'http://www.devfest.info/json/event/ag9zfmRldmZlc3RnbG9iYWxyDQsSBUV2ZW50GNKsBgw?parent_event=devfest2012&api_key=AIzaSyA2MhtOhocnrkFvc_uyavMbrLj_Qi36Vak'
_tracks = 'http://www.devfest.info/json/event/ag9zfmRldmZlc3RnbG9iYWxyDQsSBUV2ZW50GNKsBgw/tracks?parent_event=devfest2012&api_key=AIzaSyA2MhtOhocnrkFvc_uyavMbrLj_Qi36Vak'
_sessions = 'http://www.devfest.info/json/event/ag9zfmRldmZlc3RnbG9iYWxyDQsSBUV2ZW50GNKsBgw/sessions?parent_event=devfest2012&api_key=AIzaSyA2MhtOhocnrkFvc_uyavMbrLj_Qi36Vak'
_speakers = 'http://www.devfest.info/json/event/ag9zfmRldmZlc3RnbG9iYWxyDQsSBUV2ZW50GNKsBgw/speakers?parent_event=devfest2012&api_key=AIzaSyA2MhtOhocnrkFvc_uyavMbrLj_Qi36Vak'
_sponsors = 'http://www.devfest.info/json/event/ag9zfmRldmZlc3RnbG9iYWxyDQsSBUV2ZW50GNKsBgw/sponsors?parent_event=devfest2012&api_key=AIzaSyA2MhtOhocnrkFvc_uyavMbrLj_Qi36Vak'




class RoomsData(Handler):
        
    def get(self):
        logging.info('get:rooms')
        
        data = {}
        rooms = []
        
        
        room = {'id': 'lunchroom', 'name': 'Lunch Room', 'floor': '1'}
        rooms.append(room)
        
        room = {'id': 'audimax', 'name': 'AudiMax', 'floor': '1'}
        rooms.append(room)

        room = {'id': 'lobby', 'name': 'Lobby', 'floor': '1'}
        rooms.append(room)

        room = {'id': 'raum1', 'name': 'Raum 1', 'floor': '1'}
        rooms.append(room)

        room = {'id': 'raum2', 'name': 'Raum 2', 'floor': '1'}
        rooms.append(room)

        room = {'id': 'raum3', 'name': 'Raum 3', 'floor': '1'}
        rooms.append(room)

        room = {'id': 'raum4', 'name': 'Raum 4', 'floor': '1'}
        rooms.append(room)

        room = {'id': 'raum 1', 'name': 'Raum 1', 'floor': '1'}
        rooms.append(room)

        room = {'id': 'raum 2', 'name': 'Raum 2', 'floor': '1'}
        rooms.append(room)

        room = {'id': 'raum 3', 'name': 'Raum 3', 'floor': '1'}
        rooms.append(room)

        room = {'id': 'raum 4', 'name': 'Raum 4', 'floor': '1'}
        rooms.append(room)

        room = {'id': '1', 'name': 'Raum 1', 'floor': '1'}
        rooms.append(room)

        room = {'id': '2', 'name': 'Raum 2', 'floor': '1'}
        rooms.append(room)

        room = {'id': '3', 'name': 'Raum 3', 'floor': '1'}
        rooms.append(room)

        room = {'id': '4', 'name': 'Raum 4', 'floor': '1'}
        rooms.append(room)
        
        room = {'id': 'codecamp', 'name': 'Codecamp', 'floor': '1'}
        rooms.append(room)

        
        data['rooms'] = rooms
        
        self.response.headers["Content-Type"] = "application/json"
        self.response.write(json.dumps(data))
        
class SandboxData(Handler):
        
    def get(self):
        logging.info('get:rooms')
        
        data = []
        url = 'https://spreadsheets.google.com/feeds/list/%s/odb/public/basic?prettyprint=true&alt=json' % EVENT_KEY
        
        response = urllib2.urlopen(url)
        html = response.read()
        
        html = json.loads(html)


        format = ['companyname'
                    , 'companylocation'
                    , 'companydesc'
                    , 'companyurl' 
                    , 'companyproductdesc' 
                    , 'companylogo' 
                    , 'companypod' 
                  ]     
        for entry in html['feed']['entry']:
            row = entry['content']['$t'].encode('utf-8').strip()
            
            companyname = companylocation = companydesc = companyurl = companyproductdesc = companylogo = companypod = ''
            

            companyname = getRowValue(row, format, 'companyname')
            companylocation = getRowValue(row, format, 'companylocation')
            companydesc = getRowValue(row, format, 'companydesc')
            companyurl = getRowValue(row, format, 'companyurl')
            companyproductdesc = getRowValue(row, format, 'companyproductdesc')
            companylogo = getRowValue(row, format, 'companylogo')
            companypod = getRowValue(row, format, 'companypod')
            
            
            box = {
'website': companyurl,
'product_pod': companypod,
'company_description': companydesc,
'logo_vector': "",
'exhibitors': [],
'product_description': companyproductdesc,
'company_name': companyname,
'logo_img': companylogo
}
            data.append(box)            

        self.response.headers["Content-Type"] = "application/json"                                
        self.response.write(json.dumps(data))


class SponsorsDataToPlain(Handler):
        
    def get(self):
        logging.info('get:sponsors')
        logging.info('headers:%s' % self.request.headers)


        response = urllib2.urlopen('http://www.devfest.info/json/event/ag9zfmRldmZlc3RnbG9iYWxyDQsSBUV2ZW50GNKsBgw/sponsors')
        html = response.read()
        
        sponsors = json.loads(html)

        self.response.headers["Content-Type"] = "text/plain"                                
        
        DUMMY = ''
        companyname = ''
        companylocation = ''
        companydesc = ''
        companyurl = ''
        companyproductdesc = ''
        companylogo = ''
        companypod = ''
        
        self.response.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (DUMMY, companyname, companylocation, companydesc, companyurl, companyproductdesc, companylogo, companypod))
        for sponsor in sponsors:
            companyname = sponsor['company_name']
            companyurl = sponsor['website']
            companydesc = sponsor['company_description']
            #companylogo = getProfileImage()

            self.response.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (DUMMY, companyname, companylocation, companydesc, companyurl, companyproductdesc, companylogo, companypod))
        
       
class SessionsDataToPlain(Handler):
        
    def get(self):
        logging.info('get:sessions')
        logging.info('headers:%s' % self.request.headers)


        response = urllib2.urlopen('http://www.devfest.info/json/event/ag9zfmRldmZlc3RnbG9iYWxyDQsSBUV2ZW50GNKsBgw/sessions')
        html = response.read()
        
        sessions = json.loads(html)

        self.response.headers["Content-Type"] = "text/plain"                                
        
        
        self.response.write('DUMMY\tsession_date\tsession_time\tsession_room\tsession_product\tsession_track\tsession_hashtag\tsession_level\tsession_title\tsession_tags\tsession_speakers\tsession_abstract\n')
        session_date = 'Saturday November 03'
        for entry in sessions['result'][0]['events']:
            session_time = '%s - %s' % (entry['start_time'], entry['end_time'])
            session_room = entry['room'] #: "AudiMax",
            session_title = entry['title'] #: "Historie und Zukunft von GWT (Daniel Kurka)",
            session_level = entry['level'] #: "",
            session_abstract = entry['abstract'] #
            
            self.response.write('DUMMY\t' + session_date + '\t' + session_time + '\t' + session_room + '\tsession_product\tsession_track\tsession_hashtag\t' + session_level + '\t' + session_title + '\tsession_tags\tsession_speakers\t' + session_abstract + '\n')

            
 
class SessionsData(Handler):
        
    def get(self):
        logging.info('get:sessions')
        logging.info('headers:%s' % self.request.headers)
        
        
        data = {}
        data['result'] = []
                
        events = {}
        events['codelab'] = []
        events['sessions'] = []
        
        sessions = []
        result = {}
                
        response = urllib2.urlopen('https://spreadsheets.google.com/feeds/list/%s/od6/public/basic?prettyprint=true&alt=json' % EVENT_KEY)
        html = response.read()
        
        html = json.loads(html)


        format = ['sessiondate'
                    , 'sessiontime'
                    , 'sessionroom'
                    , 'sessionproduct'
                    , 'sessiontrack' 
                    , 'sessionhashtag' 
                    , 'sessionlevel' 
                    , 'sessiontitle' 
                    , 'sessiontags' 
                    , 'sessionspeakers' 
                    , 'sessionabstract' 
                  ]
        
        
        #            [sessiondate] = 
            
        for entry in html['feed']['entry']:
            
            if entry['title']['$t'] == '-':
                continue
            
            row = entry['content']['$t'].encode('utf-8').strip()
            
            id = entry['title']['$t'].encode('utf-8').replace('Row: ', '').strip()
            
            sessiondate = sessiontitle = sessiontime = sessionroom = ''
            
#            if row.find('Peter Willer') == -1:
#                continue
            sessiondate = getRowValue(row, format, 'sessiondate')
            sessiontime = getRowValue(row, format, 'sessiontime')
            sessionroom = getRowValue(row, format, 'sessionroom')
            sessionproduct = getRowValue(row, format, 'sessionproduct')
            sessiontrack = getRowValue(row, format, 'sessiontrack')
            sessionhashtag = getRowValue(row, format, 'sessionhashtag')
            sessionlevel = getRowValue(row, format, 'sessionlevel')
            
            sessiontitle = getRowValue(row, format, 'sessiontitle')
            sessiontags = getRowValue(row, format, 'sessiontags')
            sessionspeakers = getRowValue(row, format, 'sessionspeakers')
            sessionabstract = getRowValue(row, format, 'sessionabstract')

            
            '''
            parse day
            '''

            if sessiondate.find('19') > 0:
                sessiondate = '2012-10-19'
            elif sessiondate.find('20') > 0:
                sessiondate = '2012-10-20'
            elif sessiondate.find('21') > 0:
                sessiondate = '2012-10-21'
            elif sessiondate.find('03') > 0:
                sessiondate = '2012-11-03'
         
            start = sessiontime[0:sessiontime.find(' - ')]
            end = sessiontime[sessiontime.find(' - ') + 3:]

            speakers = []
            if sessionspeakers.find(','):
                sessionspeakers = sessionspeakers.split(',')
                for speaker in sessionspeakers:
                    speakers.append('devfest2012/%s/' % speaker.replace(' ', ''))
            else:
                speakers = 'devfest2012/%s/' % sessionspeakers.replace(' ', '')
                
            
            tracks = []
            if sessiontrack.find(','):
                sessiontrack = sessiontrack.split(',')
                for track in sessiontrack:
                    tracks.append(track.strip())

            else:
                tracks = sessiontrack.strip()
    
            event = {'id': "devfest2012/%s/" % id,
                        
                        'room': sessionroom,
                        'start_date': sessiondate,
                        'end_date': sessiondate,
                        
                        'start_time': start,
                        'end_time': end,
                        
                        'level': sessionlevel,
                        'track': tracks,
                        'title': sessiontitle,
                        'abstract': sessionabstract,
                        'attending': "N",
                        'tags': sessiontags,
                        'speaker_id': speakers
                        }

            
            event['has_streaming'] = False;
            event['livestream_url'] = ''; #_PmU9mpdnqM
            
            #split to different types of sessions
            isCodelab = [i for i, x in enumerate(sessiontrack) if x.find('Codecamp') != -1]
            
            logging.info('sessiontrack:%s' % sessiontrack)
            logging.info('isCodelab:%s' % isCodelab)
            
            
            if len(isCodelab) > 0:
                events['codelab'].append(event)
            else:
                events['sessions'].append(event)
            

        logging.info('codelabs:%s' % len(events['codelab']))
        logging.info('sessions:%s' % len(events['sessions']))
        
        
        result = {}
        if len(events['sessions']) > 0: 
            result['event_timeslots'] = "[{'date': '2012-06-27', 'slot1': (u'09:30', u'11:45')}, {'date': '2012-06-28', 'slot1': (u'10:00', u'11:30')}]";
            result['events'] = events['sessions']
            result['event_type'] = 'sessions'
            sessions.append(result)
        
        result = {}
        if len(events['codelab']) > 0:        
            result['event_timeslots'] = "[{'date': '2012-06-27', 'slot1': (u'09:30', u'11:45')}, {'date': '2012-06-28', 'slot1': (u'10:00', u'11:30')}]";
            result['events'] = events['codelab']
            result['event_type'] = 'codelab'
            sessions.append(result)
        
        
        
        
#        result = {}
#        events = []
#        
#        event = {
#'room': "",
#'end_date': "2012-06-27",
#'level': "Code Lab",
#'track': [
#"Code Labs 1",
#"Google Drive"
#],
#'start_time': "16:00",
#'prereq': [
#"<br>Working knowledge of Java.<br>",
#"Download and install <a href=\"https://developers.google.com/eclipse/docs/getting_started\">Eclipse, the Google Plugin for Eclipse, and the App Engine SDK for Java</a><br>"
#],
#'abstract': "Google engineers will be on-hand to help you get Google Drive integration working with your own application.  We will walk through a brief introductory sample application, with a goal of getting everyone's Drive integration up and running before the end of the session.",
#'start_date': "2012-06-27",
#'attending': "N",
#'has_streaming': False,
#'end_time': "18:00",
#'title': "Implementing Your First End-to-End Drive App",
#'id': "devfest2012/1421/",
#'tags': "Google Drive",
#'speaker_id': [
#"devfest2012/1421//devfest2012/2226"
#]
#}
#        events.append(event)
#        
#        event = {
#'room': "",
#'end_date': "2012-06-28",
#'level': "Code Lab",
#'track': [
#"Code Labs 1",
#"YouTube"
#],
#'start_time': "11:45",
#'prereq': [
#"<br>Familiarity with HTML5, JavaScript, and the jQuery library.<br>Access to a webserver (OS X's built in web sharing works, or App Engine's development server, etc.) <br> An extra credit exercise will require some experience with Python, App Engine, and SQLite (comes preinstalled on OS X and some Linux distros.<br>"
#],
#'abstract': "The YouTube Data API is changing, and we're ready to give a first look. We'll go into more details about the backend infrastructure powering the new API, as well as the new, modern libraries that will power the next generation of client code.",
#'start_date': "2012-06-28",
#'attending': "N",
#'has_streaming': False,
#'end_time': "13:30",
#'title': "Master the Latest YouTube Data API",
#'id': "devfest2012/1415/",
#'tags': "YouTube",
#'speaker_id': [
#"devfest2012/1415//devfest2012/2056",
#"devfest2012/1415//devfest2012/2293",
#"devfest2012/1415//devfest2012/2348"
#]
#}
#        events.append(event)  
#
#        result['event_timeslots'] = "[{'date': '2012-06-27', 'slot1': (u'09:30', u'11:45')}, {'date': '2012-06-28', 'slot1': (u'10:00', u'11:30')}]";
#        result['events'] = events
#        result['event_type'] = 'codelab'
#        
#        #sessions.append(result)
#        result = {}
#        events = []


        
        data['result'] = sessions
        
        data['error'] = "No auth token in request"
        
        
        
        user = users.get_current_user()
        if user:
            logging.info('Hello, ' + user.nickname())
        else:
            logging.info('Hello: anonymous')
            
        
        #etag = hashlib.sha256(response + APP_SECRET).hexdigest()
        
        #data['etag'] = "yCLeREs2Qi9VfUZLGcCchLUQ8Ys/W6k8nbDP-T9StSHXQg5D9u2ieE8"
        
        #not the best way :(
        response = json.dumps(data)
        data['etag']  = self.CreateEtag(response)
        response = json.dumps(data)
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(response)

    
class SpeakersData(Handler):
    def get(self):
        logging.info('get:speakers')
        
        data = {}
        speakers = []
        
        
#        speaker = {
#'bio': "Francesco is an Engineering Manager on the Android team responsible for device cloud messaging.",
#'first_name': "Francesco",
#'last_name': "Nerieri",
#'display_name': "Francesco Nerieri",
#'plusone_url': "https://plus.google.com/u/0/104524825852741167674/posts",
#'thumbnail_url': "http://commondatastorage.googleapis.com/io2012/headshots/nero.jpg",
#'user_id': "devfest2012/2176",
#'speaker_id': "devfest2012/100//devfest2012/2176"
#}
        #speakers.append(speaker)


        response = urllib2.urlopen('https://spreadsheets.google.com/feeds/list/%s/od7/public/basic?prettyprint=true&alt=json' % EVENT_KEY)
        html = response.read()
        
        html = json.loads(html)

        format = ['speakertitle'
                    , 'speakercompany'
                    , 'speakerabstract'
                    , 'speakerldap' 
                    , 'speakerimageurl' 
                    , 'speakerurl' 
                  ]     
        for entry in html['feed']['entry']:
            row = entry['content']['$t'].encode('utf-8').strip()
            
            speaker_title = speaker_company = speaker_abstract = speaker_ldap = speaker_image_url = speaker_url = ''
            

            speaker_title = getRowValue(row, format, 'speakertitle')
            speaker_company = getRowValue(row, format, 'speakercompany')
            speaker_abstract = getRowValue(row, format, 'speakerabstract')
            speaker_ldap = getRowValue(row, format, 'speakerldap')
            speaker_image_url = getRowValue(row, format, 'speakerimageurl')
            speaker_url = getRowValue(row, format, 'speakerurl')
            
            speaker = {
'bio': speaker_abstract,
'first_name': "",
'last_name': "",
'display_name': speaker_title,
'plusone_url': speaker_url,
'thumbnail_url': speaker_image_url,
'user_id': 'devfest2012/%s/' % speaker_title.replace(' ', ''),
'speaker_id': 'devfest2012/%s/' % speaker_title.replace(' ', '')
}
            
            speakers.append(speaker)
        
        data['devsite_speakers'] = speakers
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(data))

class CommonSlotsData(Handler):
    def get(self):
        logging.info('get:commonslots')
        
        
        data = {}
        days = []
        
        slotsparsed = {}
        slots = []
        
        
        url = 'https://spreadsheets.google.com/feeds/list/%s/od6/public/basic?prettyprint=true&alt=json' % EVENT_KEY
        
        logging.info(url)
        
        response = urllib2.urlopen(url)
        html = response.read()
        
        html = json.loads(html)


        format = ['sessiondate'
                    , 'sessiontime'
                    , 'sessionroom'
                    , 'sessionproduct'
                    , 'sessiontrack' 
                    , 'sessionhashtag' 
                    , 'sessionlevel' 
                    , 'sessiontitle' 
                    , 'sessiontags' 
                    , 'sessionspeakers' 
                    , 'sessionabstract' 
                  ]

        slot = {
'start': "07:00",
'end': "22:00",
'title': "On-site check-in",
'meta': "Level 1"
}
            
#            [sessiondate] = 
            
        slots.append(slot)

        for entry in html['feed']['entry']:
            
            if entry['title']['$t'] != '-':
                continue
            
            row = entry['content']['$t'].encode('utf-8').strip()
            
            sessiondate = sessiontitle = sessiontime = sessionroom = ''
            
#            if row.find('Peter Willer') == -1:
#                continue

            sessiondate = getRowValue(row, format, 'sessiondate')
            sessiontitle = getRowValue(row, format, 'sessiontitle')
            sessiontime = getRowValue(row, format, 'sessiontime')
            sessionroom = getRowValue(row, format, 'sessionroom')

            '''
            parse day
            '''
            if sessiondate.find('19') > 0:
                sessiondate = '2012-10-19'
            elif sessiondate.find('20') > 0:
                sessiondate = '2012-10-20'
            elif sessiondate.find('21') > 0:
                sessiondate = '2012-10-21'
            elif sessiondate.find('03') > 0:
                sessiondate = '2012-11-03'
                
            start = sessiontime[0:sessiontime.find(' - ')]
            end = sessiontime[sessiontime.find(' - ') + 3:]

            slot = {
'start': start,
'end': end,
'title': sessiontitle,
'meta': sessionroom
}
            #build sessioons array
            if not slotsparsed.has_key(sessiondate):
                slotsparsed[sessiondate] = []
            
            slotsparsed[sessiondate].append(slot)



        days = []
        data['day'] = []
        for date in slotsparsed:
        
            
            days = { 'date': date, 'slot': slotsparsed[date]}

            data['day'].append(days)

       


        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(data))     

class TracksData(Handler):
        
    def get(self):
        logging.info('get:rooms')
        
        data = {}
        tracks = []

#Cloud
#Business
#Android
#Barcamp/Workshops
#Hackathons
#Mixed
#Web

        track = {'name': 'Android', 'color': '#A6BC40', 'abstract': 'Learn about developing mobile handset and tablet apps for Android.'}
        tracks.append(track)
        
        track = {'name': "Chrome", 'color': "#46B0E2", 'abstract': "Build for the modern web with the Chrome platform."}
        tracks.append(track)

        
        #track = {'name': "Cloud Platform", 'color': "#2076BC", 'abstract': "Learn about Google's cloud offerings for developers."}
        track = {'name': "Cloud", 'color': "#2076BC", 'abstract': ""}
        tracks.append(track)

        track = {'name': "Codecamp", 'color': "#E4388F", 'abstract': "Get your hands dirty in longer, classroom-style sessions. Bring your laptop. Write code."}
        tracks.append(track)

#        track = {'name': "Hackathons", 'color': "#E4388F", 'abstract': ""}
#        tracks.append(track)


        # track = {'name': "Commerce", 'color': "#4CAA47", 'abstract': "Learn how to use Google Commerce products to improve monetization on the web, in app, and in store."}
        # tracks.append(track)

        #track = {'name': "Entrepreneurship", 'color': "#97B0DA", 'abstract': "Talks on topics related to startups, venture capital, and entrepreneurship."}

#        track = {'name': "Business", 'color': "#97B0DA", 'abstract': ""}
#        tracks.append(track)

        track = {'name': "Google APIs", 'color': "#00773F", 'abstract': "Learn about Google's various developer platforms."}
        tracks.append(track)

#        track = {'name': "Google Drive", 'color': "#F5851F", 'abstract': "Learn to develop for Google Drive and Google Apps Script."}
#        tracks.append(track)
        
        track = {'name': "Google Maps", 'color': "#4CAA47", 'abstract': "Leverage the power of Google's geospatial technology in your apps."}
        tracks.append(track)

#        track = {'name': "Google TV", 'color': "#37505C", 'abstract': "Build apps for the big screen. Learn about developing for Google TV."}
#        tracks.append(track)

        track = {'name': "Google+", 'color': "#DC4E30", 'abstract': "Learn about developing on the Google+ platform."}
        tracks.append(track)

        track = {'name': "Web", 'color': "#DC4E30", 'abstract': ""}
        tracks.append(track)


        #track = {'name': "Tech Talk", 'color': "#A1609D", 'abstract': "Tech talks on subjects such as computer science problems, programming languages, and more."}
        #tracks.append(track)
        
#        track = {'name': "BarCamp/Workshop", 'color': "#A1609D", 'abstract': "Tech talks on subjects such as computer science problems, programming languages, and more."}
#        tracks.append(track)
        
         

#        track = {'name': "YouTube", 'color': "#E72C2E", 'abstract': "Learn about developing for YouTube."}
#        tracks.append(track)
        
        
        
        data['track'] = tracks
        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(data))    
class PlacesHandler(Handler):
    def get(self):
        response = urllib2.urlopen('http://localhost:8000/places.json')
        html = response.read()
        
        places = json.loads(html)
        
        self.response.headers['Content-Type'] = 'text/plain'

        for place in places:
            self.response.out.write(place['parentID'])
            self.response.out.write('\t')
            self.response.out.write(place['locationID'])
            self.response.out.write('\t')
            self.response.out.write(place['name'])
            self.response.out.write('\t')
            self.response.out.write(place['address'])
            self.response.out.write('\t')
            self.response.out.write(place['city'])
            self.response.out.write('\t')
            self.response.out.write(place['neighborhood'])
            self.response.out.write('\t')
            self.response.out.write(place['section'])
            self.response.out.write('\t')
            self.response.out.write(place['cuisine'])
            self.response.out.write('\t')
            self.response.out.write(place['lat'])
            self.response.out.write('\t')
            self.response.out.write(place['lng'])
            self.response.out.write('\n')
            
            
            
            
    
            #"name":"181 Business (Schwabing)"
#            ,"parentID":203342
#            ,"locationID":1
#            ,"address":"Spiridon-Louis-Ring 7"
#            ,"city":"München"
#            ,"neighborhood":"Schwabing"
#            ,"section":"München"
#            ,"cuisine":"Eclectic"
#            ,"lat":48.17411
#            ,"lng":11.54718
            
        
class StatusImageHandler(Handler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
#        img_data = get_status_image_for_current_user()
#        self.response.headers["Content-Type"] = "image/png"
#        self.response.headers.add_header("Expires", "Thu, 01 Dec 1994 16:00:00 GMT")
#        self.response.out.write(img_data)

'''
common_slots.json
rooms.json
sandbox.jsonRoomsDataRoomsData
search_suggest.json
sessions.json
speakers.json
tracks.jsonCommonSlotsData
'''

app = webapp2.WSGIApplication([('/default/', MainPage)
                                , ('/default/rooms', RoomsData)
                                , ('/default/sandbox', SandboxData)
                                , ('/default/commonslots', CommonSlotsData)
                                , ('/default/sessions', SessionsData)
                                , ('/default/speakers', SpeakersData)
                                , ('/default/tracks', TracksData)
                                , ('/default/getimage', StatusImageHandler)
                                , ('/default/places', PlacesHandler)
                                
                                , ('/default/2sessions', SessionsDataToPlain)
                                , ('/default/2sponsors', SponsorsDataToPlain)
                                
        
                                
                                
                                ], debug=True)

