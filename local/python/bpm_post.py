import serial
from serial.tools.list_ports import comports as ports
import time
import http.client
import urllib.request as urllib

def postBPM(bpm):
    conn = http.client.HTTPSConnection("embebidos-2017.herokuapp.com", port=8080, timeout=5)
    conn.request("POST", "/log/" + str(bpm))
    res = conn.getresponse()
    return res

def post_bpm(bpm):
    try:
        response = urllib.urlopen('http://embebidos-2017.herokuapp.com/log/' + str(bpm))
        print ('response headers: {}'.format(response.info()))
    except IOError as e:
        if hasattr(e, 'code'): # HTTPError
            print ('http error code: ' + str(e.code))
        elif hasattr(e, 'reason'): # URLError
            print ("can't connect, reason: " + str(e.reason))
        else:
            raise

def main():
    portName = ports()[0][0]
    arduino = serial.Serial(port=portName, baudrate=115200, timeout=0.25)
    if not arduino.is_open:
        arduino.open()
    start = time.time()
    while True:
        end = start
        if arduino.in_waiting > 20:
            bpm = arduino.readline().decode('utf-8')
            bpm = bpm.strip()
            if len(bpm) == 0:
                continue
            bpm = bpm.split(':')
            if len(bpm) > 1:
                bpm = bpm[1]
            else:
                continue
            bpm = bpm.strip()
            bpm = int(bpm)
            print(bpm)
            end = time.time()
            if end - start > 15:
                print("posting BPMs ({})".format(bpm))
                post_bpm(bpm)
                start = end

        time.sleep(0.1)

if __name__ == '__main__':
    main()