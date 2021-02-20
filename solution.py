from socket import *
def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message" #this is a SMTP Program Message
    endmsg = "\r\n.\r\n"
    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    #port = 25
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    #mailserver = 'smtp.nyu.edu'
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')
    # Send HELO command and print server response.
    heloCommand = 'HELO Omar\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Send MAIL FROM command and print server response.
    # Fill in start
    mailCommand = 'MAIL FROM: <ufa2003@nyu.edu>\r\n'
    clientSocket.send(mailCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end
    # Send RCPT TO command and print server response.
    # Fill in start
    rcptCommand = 'RCPT TO: <ufa2003@nyu.edu>\r\n'
    clientSocket.send(rcptCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end
    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '354':
    #    print('354 reply not received from server.')
        # Fill in end
        # Send message data.
    msg = 'QUIT\r\n'
        # Fill in start
    #clientSocket.send(msg.encode())
    # Fill in end
    # Message ends with a single period.
    endmsg = '\r\n.\r\n'
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    #clientSocket.send(endmsg.encode())
    #recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
        # Fill in end
    # Send QUIT command and get server response.
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '221':
    #    print('221 reply not received from server.')
        # Fill in end
if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')