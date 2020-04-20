class Channel:
    def __init__(self, name, frequency, playlist):
        self.name = name
        self.frequency = frequency
        self.playlist = playlist

    def getFrequency(self):
        return self.frequency

    def __str__(self):
        return "Channel {} on {}, playlist: {}".format(
            self.name, str(self.frequency), str(self.playlist))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.name == other.name) \
                 and (self.frequency == other.frequency) and (self.playlist == other.playlist)
        else:
            return NotImplemented #False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return (self.name != other.name) \
                 or (self.frequency != other.frequency) or (self.playlist != other.playlist)
        else:
            return NotImplemented #False

    def __hash__(self):
        return hash(tuple((self.name, self.frequency)))


class Radio:
    def __init__(self, channels, frequency):
        self.channels = channels
        self.frequency = frequency

    def getCurrentFrequency(self):
        return self.frequency

    def getCurrentChannel(self):
        return self.channels[self.frequency - 0.05]
        

    
