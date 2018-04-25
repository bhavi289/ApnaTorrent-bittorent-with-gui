

# if __name__ == '__main__':

def start_downoading():
	import run
	import logging
	logging.basicConfig(level=logging.INFO)
	run = run.Run()
	run.start()
