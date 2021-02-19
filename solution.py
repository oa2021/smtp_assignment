from socket import *
debug = False

def debug_print(message):
   if debug:
      print(message)

def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message" # this is a SMTP Program Message
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
   port=25
   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   mailserver = 'smtp.nyu.edu'
   # Fill in start
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((mailserver,port))
   #serverSocket.listen(1)
   # Fill in end

   recv = clientSocket.recv(1024).decode()
   debug_print(recv)
   if recv[:3] != '220':
       debug_print('220 reply not received from server.')

   # Send HELO command and debug_print server response.
   heloCommand = 'HELO Omar\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   debug_print(recv1)
   if recv1[:3] != '250':
       debug_print('250 reply not received from server.')

   # Send MAIL FROM command and debug_print server response.
   # Fill in start
   mailCommand = 'MAIL FROM: <ufa2003@nyu.edu>\r\n'
   clientSocket.send(mailCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   debug_print(recv1)
   if recv1[:3] != '250':
      debug_print('250 reply not received from server.')

# Fill in end

   # Send RCPT TO command and debug_print server response.
   # Fill in start
   rcptCommand = 'RCPT TO: <ufa2003@nyu.edu>\r\n'
   clientSocket.send(rcptCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   debug_print(recv1)
   if recv1[:3] != '250':
      debug_print('250 reply not received from server.')
   # Fill in end

   # Send DATA command and debug_print server response.
   # Fill in start
   dataCommand = 'DATA\r\n'
   clientSocket.send(dataCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   debug_print(recv1)
   if recv1[:3] != '354':
        debug_print('354 reply not received from server.')
   # Fill in end

   # Send message data.
   # Fill in start
   clientSocket.send(msg.encode())
   #recv1 = clientSocket.recv(1024).decode()
   #debug_print(recv1)
   #if recv1[:3] != '250':
      #debug_print('250 reply not received from server.')
   # Fill in end

   # Message ends with a single period.
   # Fill in start
   clientSocket.send(endmsg.encode())
   recv1 = clientSocket.recv(1024).decode()
   debug_print(recv1)
   if recv1[:3] != '250':
      debug_print('250 reply not received from server.')
   # Fill in end

   # Send QUIT command and get server response.
   # Fill in start
   quitCommand = 'QUIT\r\n'
   clientSocket.send(quitCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   debug_print(recv1)
   if recv1[:3] != '221':
        debug_print('221 reply not received from server.')
   # Fill in end


if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')
