import threading


class EndSignalHelper:
    """
    Helper to check whether producer finished read all ID files or not

    author xiaotian
    """
    # singleton
    __instance = None

    # singleton
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(EndSignalHelper, cls).__new__(
                cls, *args, **kwargs)

            # init
            self = cls.__instance
            self.__is_end_of_ids = False
            self.__lock = threading.RLock()

        return cls.__instance

    def is_end_of_id_file(self):
        self.__lock.acquire()
        try:
            return self.__is_end_of_ids
        finally:
            self.__lock.release()

    def set_end_of_id_file_signal(self, boolean):

        self.__lock.acquire()
        try:
            self.__is_end_of_ids = boolean
        finally:
            self.__lock.release()
