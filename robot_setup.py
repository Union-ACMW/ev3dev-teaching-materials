from time import sleep
from ev3dev.ev3 import *

#
# Wrapper Functions around the ev3dev API
#

# Motor setup
left = Motor('outA')
right = Motor('outB')

# Sensor setup
touch = TouchSensor()
light = LightSensor()
ultraSensor = UltrasonicSensor()


def beep(frequency, duration):
    """
    Makes the robot play an audio tone. Note: This function is blocking!
    :param frequency: Frequency of tone play in hertz.
    :param duration: Duration to play tone in seconds.
    :return: None
    """
    Sound.tone(frequency, duration * 1000)
    sleep(duration)


def run_motors(velocity):
    """
    Sets both motors to run indefinitely.
    :param velocity: Motor velocity. Positive velocity is forward and negative is backward.
    :return: None
    """
    left.run_forever(speed_sp=velocity)
    right.run_forever(speed_sp=velocity)


def run_motors_wait(velocity, duration):
    """
    Sets both motors to run for the specified time. Note: This function is blocking!
    :param velocity: Motor velocity. Positive velocity is forward and negative is backward.
    :param duration: Duration to run motors in seconds.
    :return: None
    """
    left.run_forever(speed_sp=velocity)
    right.run_forever(speed_sp=velocity)
    sleep(duration)
    stop()


def stop():
    """
    Stops both motors.
    :return: None
    """
    left.stop()
    right.stop()


def turn_left(velocity, duration):
    """
    Sets the left motor to run for the specified duration. Note: This function is blocking!
    :param velocity: Motor velocity. Positive velocity is forward and negative is backward.
    :param duration: Duration to run motor in seconds.
    :return: None
    """
    right.stop()
    left.run_forever(speed_sp=velocity)
    sleep(duration)
    left.stop()


def turn_right(velocity, duration):
    """
    Sets the right motor to run for the specified duration. Note: This function is blocking!
    :param velocity: Motor velocity. Positive velocity is forward and negative is backward.
    :param duration: Duration to run motor in seconds.
    :return None
    """
    left.stop()
    right.run_forever(speed_sp=velocity)
    sleep(duration)
    right.stop()


def spin(velocity):
    """
    Sets the motors to spin in-place indefinitely.
    :param velocity: Motor velocity. Positive velocity is clockwise, negative is counter-clockwise.
    :return: None
    """
    left.run_forever(speed_sp=velocity)
    right.run_forever(speed_sp=-velocity)


def get_touch():
    """
    Get output from the Touch sensor.
    :return: True if the touch sensor is pressed, False Otherwise.
    """
    return touch.is_pressed


def get_light():
    """
    Get output from the Light sensor.
    :return: Ambient light value as an integer.
    """
    return light.ambient_light_intensity


def get_distance():
    """
    Get output from the Ultrasonic Sensor.
    :return: Distance to object in centimeters.
    """
    return ultraSensor.distance_centimeters
