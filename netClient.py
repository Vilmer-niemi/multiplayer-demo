import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.4"
        self.port = 5555
        self.address = (self.server, self.port)
        self.token = ''
        dataHandling.ServerReceive(self.connect())
        self.players = []
        self.position = self.findPosition()
    def findPosition(self):
        if self.token != '':
            return self.players[self.players.index(self.token)][1]
        
    def getPosition(self):
        return self.position

    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode("utf-8")
        except: 
            pass
    def send(self, message):
        try:
            self.client.send(str.encode(message))
            return self.client.recv(2048).decode("utf-8")
        except socket.error as error:
            print(error)

class dataHandling:
    def SendServer(token, x, y) -> str:
        return ",".join[str(token),str(x),str(y)]

    def SendClient(players) -> str:
        data = []
        for player in range(len(players)):
            data.append(str(players[player][0]) + "," + str(players[player][1][1])+","+str(players[player][1][1]))
        return "|".join(data)

    def ClientReceive(input:str): 
        players = []
        data = input.split('|')
        for i in range(len(data)):
            playerInfo = data[i].split(',')
            players.append([playerInfo[1], (int(playerInfo[2]),int(playerInfo[3]))])
        return players

    def ServerReceive(input:str):
        data = input.split(";")
        print(data)
        dataHandling.token = data[0]
        dataHandling.players = dataHandling.ClientReceive(data[1])
    def cordinate(input):
        if input.find("cordinate") != -1:
            return int(input.split[1]), int(input.split[2])

        print(input)