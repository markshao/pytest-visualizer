from typing import NoReturn
from typing import Dict
from collections import deque
from time import sleep
from visual.vapp import socketio


class Message(object):
    def __init__(self):
        pass


class DataHub(object):
    def __init__(self):
        self.work_thread = None
        self.__is_working = False
        self.__channels = dict()  # type: Dict[str, deque]

    @property
    def is_working(self) -> bool:
        return self.__is_working

    def ondata(self, message: Message) -> NoReturn:
        pass

    def serve(self) -> NoReturn:
        pass

    def __serve(self) -> NoReturn:
        # scan all the channels here like io-select ,later maybe use some mq middleware
        while True:
            try:
                for name, channel in self.__channels.items():
                    while True:
                        message = channel.popleft()
                        if message is None:
                            break

            finally:
                sleep(1)


class MessageSender(object):
    pass


class MessageReceiver(object):
    pass
