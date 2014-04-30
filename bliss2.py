import shlex
import subprocess
#import sys
#del sys.modules['subprocess']
#import subprocess
import webapp2




class MainHandler(webapp2.RequestHandler):

  def post(self):
    raise Exception(subprocess.__file__)
    cmds = self.request.body.split('\n')
    for cmd in cmds:
      args = shlex.split(cmd)
      proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
      (out, err) = proc.communicate()
    self.response.write("program out:" + out)
    self.response.write("program err:" + err)

app = webapp2.WSGIApplication([
    ('/.*', MainHandler)
], debug=True)


