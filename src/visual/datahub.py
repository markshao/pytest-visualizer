from typing import NoReturn
from typing import Dict
from collections import deque
from time import sleep
from flask_socketio import emit


class Message(object):
    def __init__(self):
        pass


NAMESPACE = "/test"


class DataHub(object):
    def __init__(self):
        self.__is_working = False
        self.__channels = dict()  # type: Dict[str, deque]

    @property
    def is_working(self) -> bool:
        return self.__is_working

    def ondata(self, message: Message) -> NoReturn:
        pass

    def serve(self) -> NoReturn:
        # scan all the channels here like io-select
        # later maybe use some mq middleware

        self.__is_working = True

        from visual.vapp import app

        with app.test_request_context('/'):
            while True:
                try:
                    emit("my_response", {"data": "hello world"}, namespace="/test", broadcast=True)
                finally:
                    print("sleep")
                    sleep(2)
