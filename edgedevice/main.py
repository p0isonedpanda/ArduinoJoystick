import serial
import json
import pymongo
from logger import *
import settings

set_logging(3)

def main():
    try:
        arduino = serial.Serial('/dev/ttyACM0', 9600)
        log('arduino connected')
    except:
        log('arduino not found, exiting...', 3)
        return

    try:
        client = pymongo.MongoClient('mongodb://localhost:27017',
                                     username=settings.username,
                                     password=settings.password)
        collection = client['input']['arduino']
        log('logged into mongodb')
    except:
        log('could not connect to mongodb, exiting...', 3)
        return

    # main loop
    while True:
        try:
            info = json.loads(arduino.readline())
            collection.update_one({}, { '$set' : { 'x' : info['x'], 'y' : info['y']} })
            log(collection.find_one())
        except (json.decoder.JSONDecodeError, UnicodeDecodeError):
            log('couln\'t parse json for some reason idunno, will try again', 2)

if __name__ == '__main__':
    main()
