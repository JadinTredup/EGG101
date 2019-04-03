from pyIOT import ThingSpeakBroadcastGUI
import serial.tools.list_ports


def main():
    app = ThingSpeakBroadcastGUI()
    app.run()

if __name__=="__main__":
    main()