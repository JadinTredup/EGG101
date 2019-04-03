import serial
import serial.tools.list_ports
import time
import thingspeak
import PySimpleGUI as sg

##################################################################
##                                                              ##
##             IOT/Arduino Communication Class                  ##
##                                                              ##
##################################################################

class ThingSpeaker():

    def __init__(self, channel_no, api_write_key, api_read_key):
        self.ch_write = thingspeak.Channel(channel_no, api_write_key)
        self.ch_read = thingspeak.Channel(channel_no, api_read_key)


    def connect_serial_device(self, port_name, baud_rate = 9600):
        self.ser = serial.Serial(port_name, baud_rate)


    def read_arduino(self):
        value = self.ser.readline()
        return value

    def update_static(self, value):
        try:
            self.ch_write.update({1: value})
        except:
            print('Connection Failed')

    def update_cloud(self):
        #value = self.read_arduino()
        value = 400
        self.ch_write.update({1: value})
        time.sleep(0.1)



##################################################################
##                                                              ##
##                      GUI CLASS                               ##
##                                                              ##
##################################################################

class ThingSpeakBroadcastGUI():
    """
    Class for creating GUI interfaces for broadcasting data from an Arduino, read via serial connection,
    to a Thingspeak IOT server.
    """

    def __init__(self):
        self.font = 'helvetica'
        self.RUNNING = False


    def run(self):
        """

        :return:
        """
        layout = self.create_window(win_type='info')
        window = sg.Window('EGG101 Thingspeak Application - Startup', font=(self.font, 12)).Layout(layout)
        self.RUNNING = True

        # window loop
        while self.RUNNING:
            event, values = window.Read()
            if event == 'Submit':
                #channel_no, write_key, read_key, port = values
                channel_no, write_key, read_key = values
                self.RUNNING = False
            elif event is None or event == 'Exit':
                self.RUNNING = False
                break

        window.Close()
        ts = ThingSpeaker(channel_no, write_key, read_key)
        layout = self.create_window(win_type='main')
        window = sg.Window('EGG101 Thingspeak Application - Running', font=(self.font, 12)).Layout(layout)
        #ts.connect_serial_device(port_name=port)
        self.RUNNING = True

        # Broadcasting loop
        while self.RUNNING:
            ts.update_static(400)
            event, values = window.Read()
            if event == 'Exit':
                window.Close()
                self.RUNNING = False



    def create_window(self, win_type='info'):
        """
        Create the GUI window layouts for the application.

        :param win_type: Type of GUI window to create. Others are "main"
        :return: Returns the layout object for a pysimplegui window
        """
        if win_type is 'info':
            port_list = serial.tools.list_ports.comports()
            #port_names = port_list[:][0]
            layout = [[sg.Text('EGG101 - Data Broadcaster', font=(self.font, 16), justification='center')],
                      [sg.Text('Enter Desired Channel to Connect to:', font=(self.font, 10)),
                           sg.Input(do_not_clear=True)],
                      [sg.Text('Enter API Write Key:', font=(self.font, 10)), sg.Input(do_not_clear=True)],
                      [sg.Text('Enter API Read Key:', font=(self.font, 10)), sg.Input(do_not_clear=True)],
                      #[sg.InputOptionMenu(port_names)],
                      [sg.Submit(), sg.Cancel()]]
        elif win_type is 'main':
            layout = [[sg.Text('EGG101 - Data Broadcaster', font=(self.font, 16), justification='center')],
                      [sg.Cancel()]]

        return layout
