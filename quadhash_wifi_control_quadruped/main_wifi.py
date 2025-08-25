from hashmoves import HashMoves
from machine import I2C, Pin
from time import sleep
import network
import socket

ssid = 'Your SSID'
password = 'Your Password'

sda = Pin(0)
scl = Pin(1)
id = 0
i2c = I2C(id, sda=sda, scl=scl)

hm=HashMoves()

hm.initialize(i2c)
sleep(1)
hm.initial_position()

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage(state):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>Pico Hash Control</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
            </head>
            <body>
            <div class="container">
            <h1 class="text-center">Hash Robotics</h1>
            <div class="row">
            <h2 class="text-center">QuadHash Movements</h2>
            <div style="padding:10px" class="col-sm-12">                        
            <div class="col-sm-4"><form action="./say_hi"><input class="btn btn-primary btn-lg btn-block" type="submit" value="say_hi" /></form></div>
            <div class="col-sm-4"><form action="./move_forward"><input class="btn btn-primary btn-lg btn-block" type="submit" value="move_forward" /></form></div>
            <div class="col-sm-4"><form action="./move_backward"><input class="btn btn-primary btn-lg btn-block" type="submit" value="move_backward" /></form></div>
            </div>
            <div style="padding:10px" class="col-sm-12">
            <div class="col-sm-4"><form action="./move_left"><input class="btn btn-primary btn-lg btn-block" type="submit" value="move_left" /></form></div>
            <div class="col-sm-4"><form action="./move_right"><input class="btn btn-primary btn-lg btn-block" type="submit" value="move_right" /></form></div>
            <div class="col-sm-4"><form action="./legs_spread"><input class="btn btn-primary btn-lg btn-block" type="submit" value="legs_spread" /></form></div>
            </div>
            <div style="padding:10px" class="col-sm-12">
            <div class="col-sm-4"><form action="./legs_hip_shake"><input class="btn btn-primary btn-lg btn-block" type="submit" value="legs_hip_shake" /></form></div>
            <div class="col-sm-4"><form action="./side_dance"><input class="btn btn-primary btn-lg btn-block" type="submit" value="side_dance" /></form></div>
            <div class="col-sm-4"><form action="./push_up"><input class="btn btn-primary btn-lg btn-block" type="submit" value="push_up" /></form></div>
            </div>
            <div style="padding:10px" class="col-sm-12">
            <div class="col-sm-4"><form action="./legs_hip_shake"><input class="btn btn-primary btn-lg btn-block" type="submit" value="legs_hip_shake" /></form></div>
            <div class="col-sm-4"><form action="./legs_circle_shake"><input class="btn btn-primary btn-lg btn-block" type="submit" value="legs_circle_shake" /></form></div>
            <div class="col-sm-4"><form action="./front_bow"><input class="btn btn-primary btn-lg btn-block" type="submit" value="front_bow" /></form></div>			
            </div>
            <div style="padding:10px" class="col-sm-12">
            <div class="col-sm-4"><form action="./side_step"><input class="btn btn-primary btn-lg btn-block" type="submit" value="side_step" /></form></div>
            <div class="col-sm-4"><form action="./side_wave"><input class="btn btn-primary btn-lg btn-block" type="submit" value="side_wave" /></form></div>
            <div class="col-sm-4"><form action="./legs_lift"><input class="btn btn-primary btn-lg btn-block" type="submit" value="legs_lift" /></form></div>			
            </div>
            <div style="padding:10px" class="col-sm-12">
            <div class="col-sm-4"><form action="./legs_up"><input class="btn btn-primary btn-lg btn-block" type="submit" value="legs_up" /></form></div>
            <div class="col-sm-4"><form action="./front_back_shake"><input class="btn btn-primary btn-lg btn-block" type="submit" value="front_back_shake" /></form></div>
            <div class="col-sm-4"><form action="./legs_lift"><input class="btn btn-primary btn-lg btn-block" type="submit" value="legs_lift" /></form></div>			
            </div>
            </div>
            </div>
            </body>
            </html>
            """
    return str(html)

def serve(connection):
    #Start a web server
    state = ''
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/say_hi?':
            hm.say_hi(2000,3)
        elif request =='/move_forward?':
            hm.move_forward(500,5)
        elif request =='/move_backward?':
            hm.move_backward(500,5)
        elif request =='/move_left?':
            hm.move_left(500,3)
        elif request =='/move_right?':
            hm.move_right(500,3)
        elif request =='/legs_spread?':
            hm.legs_spread(1000,5)
        elif request =='/legs_hip_shake?':
            hm.legs_hip_shake(1000,5)
        elif request =='/side_dance?':
            hm.side_dance(1000,5)
        elif request =='/push_up?':
            hm.push_up(1000,5)
        elif request =='/legs_hip_shake?':
            hm.legs_hip_shake(1000,5)
        elif request =='/legs_circle_shake?':
            hm.legs_circle_shake(1000,5)
        elif request =='/front_bow?':
            hm.front_bow(1000,1)
        elif request =='/side_step?':
            hm.side_step(1000,5)
        elif request =='/side_wave?':
            hm.side_wave(1000,5)
        elif request =='/legs_lift?':
            hm.legs_lift(1000,2)
        elif request =='/legs_up?':
            hm.legs_up(5000,1)
        elif request =='/front_back_shake?':
            hm.front_back_shake(1000,3)
            
         
        html = webpage(state)
        client.send(html)
        client.close()


try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()


