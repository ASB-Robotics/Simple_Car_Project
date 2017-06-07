import time
from threading import Thread
import Queue
import imapclient, email, threading
import SocketServer

class MyServer(SocketServer.ThreadingTCPServer):
  def __init__(self, server_address, RequestHandlerClass, qq):
    SocketServer.ThreadingTCPServer.__init__( self, server_address, RequestHandlerClass )
    self.qqq = qq

  def handle(self):
    print "here in Listen"
    self.data = self.request.recv(1024).strip()
    print self.data
    self.request.sendall( self.data.upper() + self.qqq.get())

def mymail( q ):
  imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
  imapObj.login('asb.robotics@gmail.com', 'B@nk3rb0#z17')
  imapObj.select_folder('INBOX', readonly=True)

  for i in range( 12 ):
    time.sleep(11)
    messages = imapObj.search(['NOT', 'DELETED'])
    response = imapObj.fetch(messages, ['BODY[]'])
    for msgid, data in response.iteritems():
      msg = email.message_from_string(data[b'BODY[]'])
      if 'Robot Mission' in msg['subject']:
        if msg.is_multipart():
          for payload in msg.get_payload():
            q.put( payload.get_payload() )
            break
  imapObj.logout()
  print "finished mail fetch"

q = Queue.Queue()

t1 = Thread(target=mymail, args=(q,))
t1.start()

HOST, PORT = "localhost", 9999
server = SocketServer.ThreadingTCPServer((HOST, PORT), MyServer, q)
server.serve_forever()
