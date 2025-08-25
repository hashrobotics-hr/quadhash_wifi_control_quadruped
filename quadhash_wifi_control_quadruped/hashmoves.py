from pca9685 import PCA9685
from machine import I2C, Pin
from servo import Servos
from time import sleep

class HashMoves:

    def initialize(self, i2c):
        self.pca = PCA9685(i2c=i2c)
        self.servo = Servos(i2c=i2c)
        self.servo.initial_position()

    def initial_position(self):
        pwm_array = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(2000, pwm_array)
        
    def say_hi(self, time, count):        
        pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
        pwm_array2 = [135, 45, 90, 135, 135, 180, 180, 60]
        self.servo.moveservo(time, pwm_array1)
        self.servo.moveservo(time, pwm_array2)
        for _ in range(count):
            pwm_array3 = [90, 45, 90, 135, 135, 180, 180, 60]
            pwm_array4 = [180, 45, 90, 135, 135, 180, 180, 60]
            self.servo.moveservo(time/2, pwm_array3)
            self.servo.moveservo(time/2, pwm_array4)
        pwm_array5 = [135, 45, 90, 135, 135, 180, 180, 60]
        pwm_array6 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time/2, pwm_array5)
        self.servo.moveservo(time, pwm_array6)
        
    def legs_spread(self, time, count):        
        pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array1)
        for _ in range(count):
            pwm_array2 = [135, 45, 45, 135, 60, 120, 120, 60]
            pwm_array3 = [135, 45, 45, 135, 0, 180, 180, 0]
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
        pwm_array4 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array4)
        
    def legs_hip_shake(self, time, count):        
        pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array1)
        for _ in range(count):
            pwm_array2 = [105, 15, 15, 105, 20, 160, 160, 20]
            pwm_array3 = [165, 75, 75, 165, 40, 140, 140, 40]
            pwm_array4 = [135, 45, 45, 135, 0, 180, 180, 0]
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)
        pwm_array5 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array5)
        
    def legs_circle_shake(self, time, count):        
        pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array1)
        for _ in range(count):
            pwm_array2 = [105, 75, 75, 105, 20, 160, 160, 20]
            pwm_array3 = [165, 15, 15, 165, 40, 140, 140, 40]
            pwm_array4 = [135, 45, 45, 135, 0, 180, 180, 0]
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)
        pwm_array5 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array5)
        
    def front_bow(self, time, count):
        pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
        pwm_array2 = [180, 0, 45, 135, 0, 180, 180, 0]   
        pwm_array3 = [185, 0, 45, 135, 90, 90, 180, 0]
        pwm_array4 = [180, 0, 45, 135, 0, 180, 180, 0]
        pwm_array5 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array1)
        self.servo.moveservo(time, pwm_array2)
        self.servo.moveservo(time*2, pwm_array3)
        self.servo.moveservo(time*2, pwm_array4)
        self.servo.moveservo(time, pwm_array5)

    def move_forward(self, time, count):
        for _ in range(count):
            pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
            pwm_array2 = [135, 45, 45, 90, 40, 180, 180, 20]
            pwm_array3 = [135, 45, 45, 90, 10, 180, 180, 10]
            pwm_array4 = [135, 45, 45, 90, 10, 140, 140, 10]
            pwm_array5 = [90, 45, 90, 110, 10, 120, 140, 10]
            pwm_array6 = [90, 45, 90, 110, 10, 150, 160, 10]
            pwm_array7 = [135, 90, 45, 110, 40, 150, 160, 20]
            pwm_array8 = [135, 90, 45, 110, 0, 150, 160, 0]
            pwm_array9 = [135, 45, 45, 135, 0, 180, 180, 0]

            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)
            self.servo.moveservo(time, pwm_array5)
            self.servo.moveservo(time, pwm_array6)
            self.servo.moveservo(time, pwm_array7)
            self.servo.moveservo(time, pwm_array8)
            self.servo.moveservo(time, pwm_array9)
            

    def move_backward(self, time, count):
        for _ in range(count):
            pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]  
            pwm_array2 = [90, 45, 45, 135, 20, 180, 180, 40]  
            pwm_array3 = [90, 45, 45, 135, 10, 180, 180, 10]  
            pwm_array4 = [90, 45, 45, 135, 10, 140, 140, 10]  
            pwm_array5 = [110, 90, 45, 90, 10, 140, 120, 10]  
            pwm_array6 = [110, 90, 45, 90, 10, 160, 150, 10]  
            pwm_array7 = [110, 45, 90, 135, 20, 160, 150, 40]  
            pwm_array8 = [110, 45, 90, 135, 0, 160, 150, 0]  
            pwm_array9 = [135, 45, 45, 135, 0, 180, 180, 0]
            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)
            self.servo.moveservo(time, pwm_array5)
            self.servo.moveservo(time, pwm_array6)
            self.servo.moveservo(time, pwm_array7)
            self.servo.moveservo(time, pwm_array8)
            self.servo.moveservo(time, pwm_array9)
            

    def move_left(self, time, count):
        for _ in range(count):
            pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
            pwm_array2 = [135, 45, 45, 135, 20, 180, 180, 20]
            pwm_array3 = [180, 45, 45, 180, 20, 180, 180, 20]
            pwm_array4 = [180, 45, 45, 180, 0, 180, 180, 0]
            pwm_array5 = [180, 45, 45, 180, 0, 160, 160, 0]
            pwm_array6 = [180, 90, 90, 180, 0, 160, 160, 0]
            pwm_array7 = [180, 90, 90, 180, 0, 180, 180, 0]
            pwm_array8 = [135, 45, 45, 135, 0, 180, 180, 0]
            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)
            self.servo.moveservo(time, pwm_array5)
            self.servo.moveservo(time, pwm_array6)
            self.servo.moveservo(time, pwm_array7)
            self.servo.moveservo(time, pwm_array8)

    def move_right(self, time, count):
        for _ in range(count):
            pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
            pwm_array2 = [135, 45, 45, 135, 0, 160, 160, 0]
            pwm_array3 = [135, 0, 0, 135, 0, 160, 160, 0]
            pwm_array4 = [135, 0, 0, 135, 0, 180, 180, 0]
            pwm_array5 = [135, 0, 0, 135, 20, 180, 180, 20]
            pwm_array6 = [90, 0, 0, 90, 20, 180, 180, 20]
            pwm_array7 = [90, 0, 0, 90, 0, 180, 180, 0]
            pwm_array8 = [135, 45, 45, 135, 0, 180, 180, 0]
            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)
            self.servo.moveservo(time, pwm_array5)
            self.servo.moveservo(time, pwm_array6)
            self.servo.moveservo(time, pwm_array7)
            self.servo.moveservo(time, pwm_array8)
            
    def side_dance(self, time, count):
        pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
        pwm_array2 = [90, 90, 90, 90, 0, 180, 180, 0]
        pwm_array3 = [90, 90, 90, 90, 60, 180, 120, 0]
        self.servo.moveservo(time, pwm_array1)
        self.servo.moveservo(time, pwm_array2)
        self.servo.moveservo(time, pwm_array3)
        for _ in range(count):            
            pwm_array4 = [90, 90, 90, 90, 0, 120, 180, 60]
            pwm_array5 = [90, 90, 90, 90, 60, 180, 120, 0]
            self.servo.moveservo(time, pwm_array4)
            self.servo.moveservo(time, pwm_array5)           
        pwm_array6 = [90, 90, 90, 90, 0, 180, 180, 0]
        pwm_array7 = [135, 45, 45, 135, 0, 180, 180, 0]  
        self.servo.moveservo(time, pwm_array6)
        self.servo.moveservo(time, pwm_array7)
        
        
    def push_up(self, time, count):
        pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
        pwm_array2 = [90, 90, 0, 180, 0, 180, 180, 0]
        pwm_array3 = [90, 90, 0, 180, 60, 120, 120, 60]
        self.servo.moveservo(time, pwm_array1)
        self.servo.moveservo(time, pwm_array2)
        self.servo.moveservo(time, pwm_array3)
        for _ in range(count):            
            pwm_array4 = [90, 90, 0, 180, 0, 180, 120, 60]
            pwm_array5 = [90, 90, 0, 180, 60, 120, 120, 60]
            self.servo.moveservo(time, pwm_array4)
            self.servo.moveservo(time, pwm_array5)           
        pwm_array6 = [90, 90, 0, 180, 0, 180, 180, 0]
        pwm_array7 = [135, 45, 45, 135, 0, 180, 180, 0]   
        self.servo.moveservo(time, pwm_array6)
        self.servo.moveservo(time, pwm_array7)
        
    def side_step(self, time, count):
        pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array1)
        for _ in range(count):           
            pwm_array2 = [180, 90, 90, 180, 30, 150, 150, 30]
            pwm_array3 = [90, 0, 0, 90, 0, 180, 180, 0]                       
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
        pwm_array4 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array4)
        
    def side_wave(self, time, count):
        pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
        pwm_array2 = [90, 90, 90, 90, 0, 180, 180, 0]
        pwm_array3 = [90, 90, 90, 90, 90, 150, 90, 30]
        self.servo.moveservo(time, pwm_array1)
        self.servo.moveservo(time, pwm_array2)
        self.servo.moveservo(time, pwm_array3)
        for _ in range(count):
            pwm_array4 = [90, 90, 90, 90, 30, 90, 150, 90] 
            pwm_array5 = [90, 90, 90, 90, 90, 150, 90, 30]
            self.servo.moveservo(time, pwm_array4)
            self.servo.moveservo(time, pwm_array5)
        pwm_array6 = [90, 90, 90, 90, 0, 180, 180, 0]
        pwm_array7 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time*2, pwm_array6)
        self.servo.moveservo(time*2, pwm_array7)
            
            
    def legs_lift(self, time, count):
        pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array1)
        for _ in range(count):
            pwm_array2 = [135, 0, 45, 135, 90, 180, 180, 0] 
            pwm_array3 = [135, 45, 45, 135, 0, 180, 180, 0] 
            pwm_array4 = [180, 45, 45, 135, 0, 90, 180, 0] 
            pwm_array5 = [135, 45, 45, 135, 0, 180, 180, 0]
            pwm_array6 = [135, 45, 45, 180, 0, 180, 90, 0]
            pwm_array7 = [135, 45, 45, 135, 0, 180, 180, 0]
            pwm_array8 = [135, 45, 0, 135, 0, 180, 180, 90]
            pwm_array9 = [135, 45, 45, 135, 0, 180, 180, 0]
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)
            self.servo.moveservo(time, pwm_array5)
            self.servo.moveservo(time, pwm_array6)
            self.servo.moveservo(time, pwm_array7)
            self.servo.moveservo(time, pwm_array8)
            self.servo.moveservo(time, pwm_array9)
            
    def legs_up(self, time, count):
        pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array1)
        for _ in range(count):
            pwm_array2 = [135, 45, 45, 135, 180, 0, 0, 180] 
            self.servo.moveservo(time, pwm_array2)
            sleep(2)
        pwm_array3 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array3)
        
    def front_back_shake(self, time, count):
        pwm_array1 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array1)
        for _ in range(count):
            pwm_array2 = [135, 45, 45, 135, 90, 90, 180, 0]
            pwm_array3 = [105, 15, 15, 105, 90, 90, 180, 0]#105, 75, 15, 165
            pwm_array4 = [165, 75, 75, 165, 90, 90, 180, 0]
            self.servo.moveservo(time*2, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)
        pwm_array5 = [135, 45, 45, 135, 90, 90, 180, 0]
        self.servo.moveservo(time, pwm_array5)        
        for _ in range(count):
            pwm_array6 = [135, 45, 45, 135, 0, 180, 90, 90]
            pwm_array7 = [105, 15, 15, 105, 0, 180, 90, 90]#105, 75, 15, 165
            pwm_array8 = [165, 75, 75, 165, 0, 180, 90, 90]
            self.servo.moveservo(time*2, pwm_array6)
            self.servo.moveservo(time, pwm_array7)
            self.servo.moveservo(time, pwm_array8)    
        pwm_array9 = [135, 45, 45, 135, 0, 180, 180, 0]
        self.servo.moveservo(time, pwm_array9)

            


