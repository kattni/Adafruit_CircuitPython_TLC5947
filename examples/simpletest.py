# Simple demo of controlling the TLC5947 12-bit 24-channel PWM controller.
# Will update channel values to different PWM duty cycles.
# Author: Tony DiCola
import board
import busio
import digitalio

import adafruit_tlc5947


# Define pins connected to the TLC5947
SCK = board.SCK
MOSI = board.MOSI
LATCH = board.D5

# Initialize SPI bus.
spi = busio.SPI(SCK=SCK, MOSI=MOSI)

# Initialize TLC5947
tlc5947 = adafruit_tlc5947.TLC5947(spi, digitalio.DigitalInOut(LATCH))
# You can optionally disable auto_write which allows you to control when
# channel state is written to the chip.  Normally auto_write is true and
# will automatically write out changes as soon as they happen to a channel, but
# if you need more control or atomic updates of multiple channels then disable
# and manually call write as shown below.

# There are two ways to channel channel PWM values.  The first is by getting
# a PWMOut object that acts like the built-in PWMOut and can be used anywhere
# it is used in your code.  Change the duty_cycle property to a 16-bit value
# (note this is NOT the 12-bit value supported by the chip natively) and the
# PWM channel will be updated.
pwm0 = tlc5947.create_pwm_out(0)

# Set the channel 0 PWM to 50% (32767, or half of the max 65535):
pwm0.duty_cycle = 32767
# Note if auto_write was disabled you need to call write on the parent to
# make sure the value is written (this is not common, if disabling auto_write
# you probably want to use the direct 12-bit raw access instead shown below).
#tlc5947.write()

# The other way to read and write channels is directly with each channel 12-bit
# value and an item accessor syntax.  Index into the TLC5947 with the channel
# number (0-23) and get or set its 12-bit value (0-4095).
# For example set channel 1 to 50% duty cycle.
tlc5947[1] = 2048
# Again be sure to call write if you disabled auto_write.
#tlc5947.write()