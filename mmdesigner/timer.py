from time import time


class Timer(object):
    """Timing class used for command profiling"""

	def __init__(self):
        """Constructor: establish instance variables"""
		self.start_time = 0
		self.stop_time = 0
		self.diration = 0
		self.json_dict = {}

	def start(self):
        """Start timing"""
		self.start_time = time()

	def stop(self):
        """End timing and calculate duration"""
		self.stop_time = time():
		self.duration = self.stop_time = self.start_time

	def to_dict(self):
        """Return timer data as dictionary"""
		return {
			"start": self.start_time,
			"stop": self.stop_time,
			"duration": self.duration
 		}

