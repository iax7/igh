#!/usr/bin/python
import sys
import serial
import time
import datetime
import sqlite3 as lite
import re
import console

SLEEP_TIME = 3
LAPSEMINUTES_SAVE_DB = 30
DB_FILEPATH = 'igreenhouse.db3'
ARDUINO_FILE = '/dev/ttyUSB0'

class TimeController:
    """Contains the time logic to flag to save to the db"""

    def __init__(self):
        self.next_save = datetime.datetime.now() + datetime.timedelta(minutes=LAPSEMINUTES_SAVE_DB)
        console.message.print_debug('Next save: ' + str(self.next_save))

    def isTimeToSaveDB(self):
        isTime = datetime.datetime.now() >= self.next_save
        if isTime:
            self.next_save = datetime.datetime.now() + datetime.timedelta(minutes=LAPSEMINUTES_SAVE_DB)

        return isTime
# -----Time Controller

class Sqlite:
    def __init__(self):
        try:
            self.db = lite.connect(DB_FILEPATH)
            self.cursor = self.db.cursor()
        except Exception as ex:
            console.message.print_err("Error Sqlite: " + str(ex) )
            sys.exit(1)

    def commit(self):
        self.db.commit()

    def query(self, sql):
        rows = []
        try:
            cur = self.cursor
            cur.execute(sql)

            # print "the first element in rows will be the column names."
            column_names = [x[0] for x in cur.description]
            rows.append(column_names)

            while True:
                row = cur.fetchone()
                if row is None:
                    break

                rows.append(row)
        except lite.Error, e:
            console.message.print_err("Error %s:" % e.args[0])
            sys.exit(1)

        return rows

class Arduino:
    def __init__(self):
        self.regex = re.compile(';(([A-Z]*):([0-9.]*))')
        self.measures_list = ['SH', 'R', 'RT', 'RH']
        self.dictionary = {}
        for item in self.measures_list:
            self.dictionary[item] = []

        try:
            self.ser = serial.Serial(ARDUINO_FILE, 9600)
            console.message.print_debug("Arduino initializated!")
        except Exception as ex:
            console.message.print_err("Error Arduino: " + str(ex) )
            console.message.print_err("               " + str(type(ex)))
            sys.exit(1)

    def readln(self):
        return self.ser.readline()

    def clear(self):
        self.dictionary.clear()
        for item in self.measures_list:
            self.dictionary[item] = []

    def values_average(self):
        for item in self.dictionary.keys():
            self.dictionary[item] = Arduino.avg(self.dictionary[item])

    @classmethod
    def simulate(cls, integer=0):
        #RegEx Result=[('SH:145', 'SH', '145'), ('R:1023', 'R', '1023'), ('RT:28.00', 'RT', '28.00'),
                    #  ('RH:56.00', 'RH', '56.00')]
        return ';SH:'+str(145+integer)+';R:'+str(1023+integer)+';RT:'+str(28.00+integer)+';RH:'+str(56.00+integer)+''

    @classmethod
    def avg(cls, list):
        sum = 0.0
        for i in list:
            sum += i

        return sum/len(list)

def main():
    timeController = TimeController()
    arduino = Arduino()
    while True:
        arduino_raw = arduino.readln() #Arduino.simulate()
        regex_result = arduino.regex.findall(arduino_raw)
        print arduino_raw

        for tuple in regex_result:
            #console.message.print_debug(tuple)
            arduino.dictionary[tuple[1]].append(float(tuple[2]))

        #If LAPSEMINUTES_SAVE_DB is met save & reset
        if timeController.isTimeToSaveDB():
            console.message.print_debug("Time to save to DB " + str(datetime.datetime.now()))
            arduino.values_average()
            console.message.print_debug('Avg:' + str(arduino.dictionary))

            gh = [1, datetime.datetime.now(), arduino.dictionary['RT'], arduino.dictionary['RH'],arduino.dictionary['R']]
            sh = [1, datetime.datetime.now(), arduino.dictionary['SH']]
            #save to db
            sql = Sqlite()
            sql.cursor.execute("INSERT INTO ghdata('ghId','Measured','Temperature','Humidity','Rain') VALUES (?,?,?,?,?)", gh)
            sql.cursor.execute("INSERT INTO soil('PotId','Measured','Humidity') VALUES (?,?,?)", sh)
            sql.commit()
            arduino.clear() #Resets arduino values

        #print ".",
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()
