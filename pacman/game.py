from abc import ABCMeta, abstractmethod


class Game(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def process_rules(self):
        pass

    @abstractmethod
    def process_events(self, events):
        for e in events:
            if e.type == pygame.QUIT:
                exit()