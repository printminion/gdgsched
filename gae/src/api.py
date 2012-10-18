import os
import sys
import webapp2
import jinja2
import logging
from google.appengine.api import users
from secrets import SESSION_KEY
#from handlers import BaseRequestHandler
from google.appengine.api import oauth

# Note, unlike in the Android app below, there's no 'oauth2:' prefix here
SCOPE = 'https://www.googleapis.com/auth/userinfo.email'


# webapp2 config
app_config = {
  'webapp2_extras.sessions': {
    'cookie_name': '_simpleauth_sess',
    'secret_key': SESSION_KEY
  },
  'webapp2_extras.auth': {
    'user_attributes': []
  }
}

# inject './lib' dir in the path so that we can simply do "import ndb" 
# or whatever there's in the app lib dir.
if 'lib' not in sys.path:
    sys.path[0:0] = ['lib']
    
    
    
APP_ID = ''
template_dir = os.path.join(os.path.dirname(__file__), 'templates/' + APP_ID)
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir)
                               , autoescape=True)

class Handler(webapp2.RedirectHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
    
        
class MainPage(Handler):
    def render_front(self):
        self.render("index.html")
        
    def get(self, params):
        logging.info('get:%s' % params)
                
        self.render_front()

    def post(self, params):
        logging.info('post:%s' % params)
                
        self.render_front()
        
class ApiHandlerSpeakers(Handler):
    def get(self, params):
        logging.info('get:%s' % params)
        logging.info('header:%s' % self.request)
        
#Authorization: Bearer ya29.AHES6ZRS8N-yaKFA-RQVmTDxUPy8wIWxOwI5-BHDmJ_yoJWFu3NX7loX
#Connection: Keep-Alive
#Host: 192.168.178.42:8082
#User-Agent: gdg.devfest.app/0.19 (19) (gzip)
                
        self.response.headers["Content-Type"] = "application/json"
        self.render("speakers.json")

    def post(self, params):
        logging.info('post:%s' % params)
        logging.info('header:%s' % self.request)
        
        self.response.headers["Content-Type"] = "application/json"
        self.render("speakers.json")



class ApiHandlerSessions(Handler):
#class ApiHandlerSessions(BaseRequestHandler):
    def get(self, params):
        logging.info('get:%s' % params)
        logging.info('header:%s' % self.request)
        
#Authorization: Bearer ya29.AHES6ZRS8N-yaKFA-RQVmTDxUPy8wIWxOwI5-BHDmJ_yoJWFu3NX7loX
#Connection: Keep-Alive
#Host: 192.168.178.42:8082
#User-Agent: gdg.devfest.app/0.19 (19) (gzip)
        user = users.get_current_user()
        if user:
            logging.info('Hello, ' + user.nickname())
        else:
            logging.info('Hello: anonymous')
            
        """Handles GET /profile"""    
#        if self.logged_in:
#            logging.info('Hello, simpleauth: %s' % self.current_user)
#        else:
#            logging.info('Hello: simpleauth:anonymous')
            
        # magic happens here
#        SCOPE = 'https://www.googleapis.com/auth/userinfo.email'
#        SCOPE = 'https://www.googleapis.com/auth/userinfo.profile'
#        user = oauth.get_current_user(SCOPE)
#        if user:
#            logging.info('oauth: %s' % user.email())
#        else:
#            logging.info('oauth: anonymous')
#        

            
        self.response.headers["Content-Type"] = "application/json"
        self.render("sessions.json")

    def post(self, params):
        logging.info('post:%s' % params)
        logging.info('header:%s' % self.request)
        
        self.response.headers["Content-Type"] = "application/json"
        self.render("sessions.json")
        
class ApiHandlerMySchedule(Handler):
    def get(self, params):
        logging.info('get:%s' % params)
        logging.info('header:%s' % self.request)
        
        self.response.headers["Content-Type"] = "application/json"
        self.render("myschedule.json")

    def post(self, params):
        logging.info('post:%s' % params)
        logging.info('header:%s' % self.request)
        
        
#Authorization: Bearer ya29.AHES6ZRS8N-yaKFA-RQVmTDxUPy8wIWxOwI5-BHDmJ_yoJWFu3NX7loX
#Connection: Keep-Alive
#Content-Length: 30
#Content-Type: application/json
#Content_Length: 30
#Content_Type: application/json
#Host: 192.168.178.42:8082
#User-Agent: gdg.devfest.app/0.19 (19) (gzip)
#
#{"sessionid":"gooio2012/315/"}

        
        self.response.headers["Content-Type"] = "application/json"
        self.render("myschedule.json")

class ApiHandlerAnnouncements(Handler):
    def get(self, params):
        logging.info('get:%s' % params)
        logging.info('header:%s' % self.request)
        
        self.response.headers["Content-Type"] = "application/json"
        self.render("announcements.json")

    def post(self, params):
        logging.info('post:%s' % params)
        logging.info('header:%s' % self.request)
        
        self.response.headers["Content-Type"] = "application/json"
        self.render("announcements.json")

class ApiHandlerSandboxData(Handler):
    def get(self, params):
        logging.info('get:%s' % params)
        logging.info('header:%s' % self.request)
        
        self.response.headers["Content-Type"] = "application/json"
        self.render("sandbox-data.json")

    def post(self, params):
        logging.info('post:%s' % params)
        logging.info('header:%s' % self.request)
        
        self.response.headers["Content-Type"] = "application/json"
        self.render("sandbox-data.json")

#    private static final String BASE_URL = "https://google-developers.appspot.com/_ah/api/resources/v0.1";
#    public static final String GET_ALL_SESSIONS_URL      = BASE_URL + "/sessions?parent_event=" + ROOT_EVENT_ID + "&api_key=" + CONFERENCE_API_KEY;
#    public static final String GET_ALL_SPEAKERS_URL      = BASE_URL + "/speakers?event_id=" + ROOT_EVENT_ID + "&api_key=" + CONFERENCE_API_KEY;
#    public static final String GET_ALL_ANNOUNCEMENTS_URL = BASE_URL + "/announcements?parent_event=" + ROOT_EVENT_ID + "&api_key=" + CONFERENCE_API_KEY;
#    public static final String EDIT_MY_SCHEDULE_URL      = BASE_URL + "/editmyschedule/o/";
    
app = webapp2.WSGIApplication([('/api/sandbox-data(.*)', ApiHandlerSandboxData)
                               , ('/api/events/io/sandbox-data(.*)', ApiHandlerSandboxData)
                               , ('/api/sessions(.*)', ApiHandlerSessions)
                               , ('/api/speakers(.*)', ApiHandlerSpeakers)
                               , ('/api/announcements(.*)', ApiHandlerAnnouncements)
                               , ('/api/editmyschedule/o/(.*)', ApiHandlerMySchedule)
                               ], config=app_config, debug=True)


