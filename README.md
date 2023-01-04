# User Guide

## TU20D

### Appearance

TU20D is this guy.

![IMG_4896](https://user-images.githubusercontent.com/95418272/210528535-db88acc2-c52d-4564-8fb1-f94e6e041c34.JPG)


### User Interface

This package has a GUI. So the most important thing is to start the GUI.

#### Connection

1. [Install RS232 Drive](https://download2261.mediafire.com/jhcwmy0358pg/k5mkp4azlygnyad/PL2303GT(3).rar)

2. Connect your laptop to TU20D via RS232 to USB cable

#### Demo Code

```python
from LabGadgetsLib import GUI
GUI.startGUI()
```

#### Operation Parameters

- T --- Get Temperature
- D --- Get Device's name

- S --- e.g. S+0030.00\r\n

## especBTU133

### Appearance

BTU133 is this guy.

![IMG_5207](https://user-images.githubusercontent.com/95418272/210528558-dc65e68c-be3a-4b68-bd78-0dec522e2289.JPG)


### User Interface

There is a server in BTU-133. The program file that needs to be uploaded to the server is a json file.

The main function of this python package is to create such a json file.

#### Demo Code

```python
from Espec import especBTU133 as BTU
hh = BTU.Program(prog_name="DemoProg233", deviation=1.0)
hh.instant(set_value=40)
hh.soak(time=[0, 1, 0], gs='false')
hh.end(stop_chamber="on")
hh.export()
```

#### soak(time, gs)

##### Function

Keep the temperature constant at the last set point.

##### Args

- **time:** Duration time in [hours, minutes, seconds] format. The upper limit is [999,59,59].

- **gs:** gs is shorted for Guaranteed Soak. It decides whether the program should meet with the deviation or not. Default value for gs is "false", which means program doesn't meet with the deviation. Also, you can set gs="true".

#### ramp_rate(rate, set_value, gs)

##### Function

The temperature changes at a given rate to the set point.

##### Args

- **rate:** Rate of temperature change. Shouldn't be negative.

- **set_value:** User's expected temperature.

- **gs:** gs is shorted for Guaranteed Soak. It decides whether the program should meet with the deviation or not. Default value for gs is "false", which means program doesn't meet with the deviation. Also, you can set gs="true".

#### ramp_time(time, set_value, gs)

##### Function

The temperature gradually rises to the set point within a specified period of time.

##### Args

- **time:** Duration time in [hours, minutes, seconds] format. The upper limit is [999,59,59].
- **set_value:** User's desired temperature.

- **gs:** gs is shorted for Guaranteed Soak. It decides whether the program should meet with the deviation or not. Default value for gs is "false", which means program doesn't meet with the deviation. Also, you can set gs="true".

#### instant(set_value)

##### Function

Change the set_value immediately. Usually used followed by soak.

##### Args

- **set_value:** User's desired temperature.

#### jump(jump_step, jump_count)

##### Function

Form a control loop.

##### Args

- **jump_step:** The index of the step that you want to jump to.
- **jump_count:** How many times does the program jump. 0 for countless times.

#### end(end_action, stop_chamber)

##### Function

The last step of a program.

##### Args

- **end_action:**
- **stop_chamber:** Don't close the chamber: stop_chamber = "off"; Close the chamber: stop_chamber = "on"



> At last, writing this guidence document is more laborious than writing code for me.
>
> _ (:_」∠) _
