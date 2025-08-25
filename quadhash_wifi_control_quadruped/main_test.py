from hashmoves import HashMoves
from machine import I2C, Pin
from time import sleep


sda = Pin(0)
scl = Pin(1)
id = 0
i2c = I2C(id, sda=sda, scl=scl)


hm=HashMoves()

hm.initialize(i2c)

hm.initial_position()
sleep(1)

hm.say_hi(2000,3)
hm.move_forward(500,5)
hm.move_backward(500,5)
hm.move_left(500,3)
hm.move_right(500,3)
hm.legs_spread(1000,5)
hm.legs_hip_shake(1000,5)
hm.side_dance(1000,5)
hm.push_up(1000,5)
hm.legs_hip_shake(1000,5)
hm.legs_circle_shake(1000,5)
hm.front_bow(1000,1)
hm.side_step(1000,5)
hm.side_wave(1000,5)
hm.legs_lift(1000,2)
hm.legs_up(5000,1)
hm.front_back_shake(1000,3)


