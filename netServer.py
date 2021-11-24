import socket, os, binascii
from _thread import *
from netClient import dataHandling
# server ip and port - configuration
server = "192.168.1.4"
port = 5555
playerdata = []
def addPlayer(coordinate:tuple, token:str, address):

    playerdata.append({"coordinate":coordinate,"token":token,"address":address})
def updatePlayer(data:tuple, player):
    playerdata[playerdata.index(player["token"])] = {"coordinate":data,"token":player["token"], "address":player["address"]}
def removePlayer(player):
    playerdata.remove(playerdata.index(player["token"]))
def getPlayers():
    data = []
    for player in range(len(playerdata)):
        data.append([playerdata[player]["token"], playerdata[player]["coordinate"]])    
    return data

socketWrench = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socketWrench.bind((server, port))
except socket.error as error:
    print(error)
socketWrench.listen(10) 
print("Listening for connections")
def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()  
    
def send(connection):
    connection.sendall(str.encode(dataHandling.SendClient()))
def client(connection, player, address):
    while True:
        try:
            data = dataHandling.ServerReceive(connection.recv(2048).decode())
            updatePlayer(data, player)
            send(connection)
            if not data:
                print(address,"disconnected")
                break
        except:
            break
    print(address,"Lost")
    removePlayer(player)

    connection.close()
playerindex = -1
while True:
    playerindex += 1
    connection, address = socketWrench.accept()
    print(address,"Added")
    token = generate_key()
    addPlayer((0,0),token,address)
    connection.send(str.encode(token+";"+"data," + dataHandling.SendClient(getPlayers())))
    
    start_new_thread(client, (playerdata[playerindex],address,))