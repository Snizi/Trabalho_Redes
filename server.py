import socket
from _thread import *
from player import Player
import pickle

server = "172.18.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("Waiting for a connection, Server Started")


players = [Player(0,0, (255,0,0)), Player(100,100,(0,0,255)), Player(150,150,(0,255,0))]

def threaded_client(conn, player_id):
    conn.send(pickle.dumps(players[player_id]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))
            players[player_id] = data

            if not data:
                print("Disconnected")
                break
            else:
                # if player_id == 0:
                #     reply = [players[1], players[2]]
                # if player_id == 1 :
                #     reply = [players[0], players[2]]
                # else:
                #     reply = [players[1], players[0]]
                
                reply = [players[0], players[1], players[2]]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1