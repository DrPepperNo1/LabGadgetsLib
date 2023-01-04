#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/01/03 22:06
# @Author  : YuXia
# @Email   : yxia404@ucsb.edu
# @File    : main.py
import json


class Program:
    def __init__(self, prog_name="Program_1", deviation=3.0):
        '''
        This class is used to create program files of Espec BTU-133 that ends in .json
        Args:
            prog_name: name of program file. Not include .json.
            deviation: Tolerance between current point and set point. The value shouldn't be negative.
        '''
        self.prog_name = prog_name
        self.deviation = deviation
        self.steps = {"type": "watlow_f4t", "name": self.prog_name, "log": "false",
                      "guaranteed_soak": {"loop_1": self.deviation, "loop_2": 10, "loop_3": 10, "loop_4": 10},
                      "steps": []
                      }

        self.set_value = 0

    def clear(self):
        self.steps = {"type": "watlow_f4t", "name": self.prog_name, "log": "false",
                      "guaranteed_soak": {"loop_1": self.deviation, "loop_2": 10, "loop_3": 10, "loop_4": 10},
                      "steps": []
                      }

    def export(self):
        '''

        Export .json file. Then user should upload this file to the Web Controller(IP:192.168.0.83).

        '''
        jsonString = json.dumps(self.steps, indent=2)
        with open(self.prog_name + ".json", "w") as jsonFile:
            jsonFile.write(
                jsonString.replace('"false"', 'false').replace('"true"',
                                                               'true'))  # Use replace to write false into json without quotes.
            jsonFile.close()

    # Specific Steps
    def soak(self, time=[0, 0, 0], gs="false"):
        '''
        Keep the temperature constant at the last set point.
        Args:
            time: Duration time in [hours, minutes, seconds] format. The upper limit is [999,59,59].
            gs: gs is shorted for Guaranteed Soak.
                It decides whether the program should meet with the deviation or not.
                Default value for gs is "false", which means program doesn't meet with the deviation.
                Also, you can set gs="true".

        Returns:

        '''
        if time[0] < 1000 and time[0] >= 0 and time[1] < 60 and time[1] >= 0 and time[2] < 60 and time[2] >= 0:
            self.steps["steps"].append({
                "type": "soak",
                "duration": "PT" + str(time[0]) + "H" + str(time[1]) + "M" + str(time[2]) + "S",
                "jump_step": 1,
                "jump_count": 1,
                "loop_1": {
                    "rate": 0,
                    "set_value": self.set_value,
                    "guaranteed_soak": gs,
                    "end_action": "user"
                },
                "loop_2": {
                    "rate": 0,
                    "set_value": 0,
                    "guaranteed_soak": "false",
                    "end_action": "user"
                },
                "loop_3": {
                    "rate": 0,
                    "set_value": 0,
                    "guaranteed_soak": "false",
                    "end_action": "user"
                },
                "loop_4": {
                    "rate": 0,
                    "set_value": 0,
                    "guaranteed_soak": "false",
                    "end_action": "user"
                },
                "wait_1": {
                    "condition": "none",
                    "value": 0
                },
                "wait_2": {
                    "condition": "none",
                    "value": -3.761609275977344e-37
                },
                "wait_3": {
                    "condition": "none",
                    "value": 0
                },
                "wait_4": {
                    "condition": "none",
                    "value": -3.761609275977344e-37
                },
                "event_1": "off",
                "event_2": "off",
                "event_3": "off",
                "event_4": "off",
                "event_5": "off",
                "event_6": "off",
                "event_7": "off",
                "event_8": "off"
            })
        else:
            raise ValueError("Wrong Time Range.")

    def ramp_rate(self, rate=0, set_value=0, gs="false"):
        '''
        The temperature changes at a given rate to the set point.
        Args:
            rate: Rate of temperature change. Shouldn't be negative.
            set_value: User's expected temperature.
            gs: gs is shorted for Guaranteed soak.
                It decides whether the program should meet with the deviation or not.
                Default value for gs is "false", which means program doesn't meet with the deviation.
                Also, you can set gs="true".

        Returns:

        '''
        self.set_value = set_value
        self.steps["steps"].append({
            "type": "ramp_rate",
            "duration": "PT0H0M0S",
            "jump_step": 1,
            "jump_count": 1,
            "loop_1": {
                "rate": rate,
                "set_value": self.set_value,
                "guaranteed_soak": gs,
                "end_action": "user"
            },
            "loop_2": {
                "rate": 0,
                "set_value": 0,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "loop_3": {
                "rate": 0,
                "set_value": 0,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "loop_4": {
                "rate": 0,
                "set_value": 0,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "wait_1": {
                "condition": "none",
                "value": 0
            },
            "wait_2": {
                "condition": "none",
                "value": -3.761609275977344e-37
            },
            "wait_3": {
                "condition": "none",
                "value": 0
            },
            "wait_4": {
                "condition": "none",
                "value": -3.761609275977344e-37
            },
            "event_1": "off",
            "event_2": "off",
            "event_3": "off",
            "event_4": "off",
            "event_5": "off",
            "event_6": "off",
            "event_7": "off",
            "event_8": "off"
        })

    def ramp_time(self, time=[0, 0, 0], set_value=0, gs="false"):
        '''
        The temperature gradually rises to the set point within a specified period of time.
        Args:
            time: Duration time in [hours, minutes, seconds] format. The upper limit is [999,59,59].
            set_value: User's expected temperature.
            gs: gs is shorted for Guaranteed soak.
                It decides whether the program should meet with the deviation or not.
                Default value for gs is "false", which means program doesn't meet with the deviation.
                Also, you can set gs="true".

        Returns:

        '''
        self.set_value = set_value
        if time[0] < 1000 and time[0] >= 0 and time[1] < 60 and time[1] >= 0 and time[2] < 60 and time[2] >= 0:
            self.steps["steps"].append({
                "type": "ramp_time",
                "duration": "PT" + str(time[0]) + "H" + str(time[1]) + "M" + str(time[2]) + "S",
                "jump_step": 1,
                "jump_count": 1,
                "loop_1": {
                    "rate": 0,
                    "set_value": self.set_value,
                    "guaranteed_soak": gs,
                    "end_action": "user"
                },
                "loop_2": {
                    "rate": 0,
                    "set_value": 0,
                    "guaranteed_soak": "false",
                    "end_action": "user"
                },
                "loop_3": {
                    "rate": 0,
                    "set_value": 0,
                    "guaranteed_soak": "false",
                    "end_action": "user"
                },
                "loop_4": {
                    "rate": 0,
                    "set_value": 0,
                    "guaranteed_soak": "false",
                    "end_action": "user"
                },
                "event_1": "off",
                "event_2": "off",
                "event_3": "off",
                "event_4": "off",
                "event_5": "off",
                "event_6": "off",
                "event_7": "off",
                "event_8": "off",
                "wait_1": {
                    "condition": "none",
                    "value": 0
                },
                "wait_2": {
                    "condition": "none",
                    "value": 0
                },
                "wait_3": {
                    "condition": "none",
                    "value": 0
                },
                "wait_4": {
                    "condition": "none",
                    "value": 0
                }
            })
        else:
            raise ValueError("Wrong Time Range.")

    def instant(self, set_value=0):
        '''
        Change the set_value immediately. Usually used followed by soak.
        Args:
            set_value: User's desired temperature.

        Returns:

        '''
        self.set_value = set_value
        self.steps["steps"].append({
            "type": "instant",
            "duration": "PT0H0M0S",
            "jump_step": 1,
            "jump_count": 1,
            "loop_1": {
                "rate": 0,
                "set_value": self.set_value,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "loop_2": {
                "rate": 0,
                "set_value": 0,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "loop_3": {
                "rate": 0,
                "set_value": 0,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "loop_4": {
                "rate": 0,
                "set_value": 0,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "wait_1": {
                "condition": "none",
                "value": 0
            },
            "wait_2": {
                "condition": "none",
                "value": -3.761609275977344e-37
            },
            "wait_3": {
                "condition": "none",
                "value": 0
            },
            "wait_4": {
                "condition": "none",
                "value": -3.761609275977344e-37
            },
            "event_1": "off",
            "event_2": "off",
            "event_3": "off",
            "event_4": "off",
            "event_5": "off",
            "event_6": "off",
            "event_7": "off",
            "event_8": "off"
        })

    def jump(self, jump_step=1, jump_count=1):
        '''
        Form a control loop.
        Args:
            jump_step: The index of the step that you want to jump to.
            jump_count: How many times does the program jump. 0 for countless times.

        Returns:

        '''
        self.steps["steps"].append({
            "type": "jump",
            "duration": "PT0H0M0S",
            "jump_step": jump_step,
            "jump_count": jump_count,
            "loop_1": {
                "rate": 0,
                "set_value": self.set_value,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "loop_2": {
                "rate": 0,
                "set_value": 0,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "loop_3": {
                "rate": 0,
                "set_value": 0,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "loop_4": {
                "rate": 0,
                "set_value": 0,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "wait_1": {
                "condition": "none",
                "value": 0
            },
            "wait_2": {
                "condition": "none",
                "value": -3.761609275977344e-37
            },
            "wait_3": {
                "condition": "none",
                "value": 0
            },
            "wait_4": {
                "condition": "none",
                "value": -3.761609275977344e-37
            },
            "event_1": "off",
            "event_2": "off",
            "event_3": "off",
            "event_4": "off",
            "event_5": "off",
            "event_6": "off",
            "event_7": "off",
            "event_8": "off"
        })

    def end(self, end_action="user", stop_chamber="off"):
        '''
        The last step of a program.
        Args:
            end_action:
            stop_chamber: Don't close the chamber: stop_chamber = "off"
                          Close the chamber: stop_chamber = "on"

        Returns:

        '''
        self.steps["steps"].append({
            "type": "end",
            "duration": "PT0H0M0S",
            "jump_step": 1,
            "jump_count": 1,
            "loop_1": {
                "rate": 0,
                "set_value": self.set_value,
                "guaranteed_soak": "false",
                "end_action": end_action
            },
            "loop_2": {
                "rate": 0,
                "set_value": 0,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "loop_3": {
                "rate": 0,
                "set_value": 0,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "loop_4": {
                "rate": 0,
                "set_value": 0,
                "guaranteed_soak": "false",
                "end_action": "user"
            },
            "wait_1": {
                "condition": "none",
                "value": 0
            },
            "wait_2": {
                "condition": "none",
                "value": -3.761609275977344e-37
            },
            "wait_3": {
                "condition": "none",
                "value": 0
            },
            "wait_4": {
                "condition": "none",
                "value": -3.761609275977344e-37
            },
            "event_1": "off",
            "event_2": "off",
            "event_3": "off",
            "event_4": "off",
            "event_5": "off",
            "event_6": "off",
            "event_7": "off",
            "event_8": stop_chamber
        })


