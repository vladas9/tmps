class GameManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance
