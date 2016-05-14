#!/usr/bin/env python3

import logging

from .ScreenBase import ScreenBase

class LargeClock(ScreenBase):
    def createWidgets(self):
        self.pin = self.intConfig('sensorPort', 18)
        
        self.h1 = self.screen.add_number_widget("h1", x=1, value=0)
        self.h2 = self.screen.add_number_widget("h2", x=4, value=0)
        self.m1 = self.screen.add_number_widget("m1", x=8, value=0)
        self.m2 = self.screen.add_number_widget("m2", x=11, value=0)

        self.dataSources['DateTime'].attach('LargeClock', self.updateTime)

        self.dot1 = self.screen.add_string_widget("d1", ".", x=7, y=1)
        self.dot2 = self.screen.add_string_widget("d2", ".", x=7, y=2) 

        self.temp = self.screen.add_string_widget("temp", '--', x=15, y=1)
        self.humidity = self.screen.add_string_widget("humidity", '--', x=15, y=2)
        self.dataSources['AM2302'].attach('LargeClock', self.updateTemp)

    def updateTime(self, data):
        self.lcdLock.acquire()
        self.h1.set_value(data.hour / 10)
        self.h2.set_value(data.hour % 10)

        self.m1.set_value(data.minute / 10)
        self.m2.set_value(data.minute % 10)
        self.lcdLock.release()

    def updateTemp(self, data):
        if data[0]:
            self.lcdLock.acquire()
            self.humidity.set_text("{0:02.0f}".format(data[0]))
            self.temp.set_text("{0:02.0f}".format(data[1]))
            self.lcdLock.release()