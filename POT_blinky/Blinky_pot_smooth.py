from machine import Pin, ADC
import time

led = Pin(15, Pin.OUT)
adc = ADC(26)

def smooth_adc(sample=10): #Sampling for less spikes and dips
    sum = 0
    for x in range(sample):
        sum += adc.read_u16()
        time.sleep(0.01)
    avg = sum // sample
    return avg

while True:
    pot_val = smooth_adc()/65535 #Range is 0–65535, dividing makes it 0-1
    print("Pot Value: ", {pot_val})
    
    led.toggle()
    time.sleep(pot_val)