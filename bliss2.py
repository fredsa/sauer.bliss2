import logging
logging.error('TESTING')

try:
  import shlex
  import subprocess
  #import sys
  #del sys.modules['subprocess']
  #import subprocess
  import webapp2
except Exception, e:
  logging.error('Oops: {}'.format(e))



class MainHandler(webapp2.RequestHandler):

  def post(self):
    # raise Exception(subprocess.__file__)
    cmds = self.request.body.split('\n')
    for cmd in cmds:
      args = shlex.split(cmd)
      proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
      (out, err) = proc.communicate()
    self.response.write("program out: {}".format(out))
    self.response.write("program err: {}".format(err))

app = webapp2.WSGIApplication([
    ('/.*', MainHandler)
], debug=True)


