from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import subprocess
from threading import Thread
from Scripts.main import start_downoading
import threading, traceback
from multiprocessing import Process
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.

# torrent_download = threading.Thread(target=start_downoading)
torrent_download = Process(target=start_downoading)
def Home(request):

	# output = script_function() 
	# return HttpResponse(output)
	if request.method == 'GET':
		return render(request,'home/home.html')
	elif request.method == 'POST':
		print "POST Successfull"
		# torrent_download = threading.Thread(target=start_downoading)
	 	torrent_download.daemon = True
	 	torrent_download.start()
	 	return render(request,'home/downloading.html')
	 	# output = script_function() 
		return HttpResponse("Downloading")
	# return HttpResponse("Hi")

def Downloading(request):
	if request.method == 'POST':
		print "Stop Thread"
		torrent_download.terminate()
		return HttpResponse("Stopped Downloading!")

def script_function():
	print subprocess
	return subprocess.call(['python', 'Scripts/main.py'])
  # return subprocess.call(['subprocess.py'])

  # return subprocess.check_call(['/Scripts/main.py'])

def DownloadPercentage(request):
	if request.method == 'GET':
		obj = get_object_or_404(TorrentDownload, id=1)
		print "in view",obj
		return obj.percentage

