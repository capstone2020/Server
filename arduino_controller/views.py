from django.shortcuts import render
import os

# Create your views here.

def post_list(request):
	if request.method == "POST":
		print("Recieved POST")
#		os.system('arduino --upload ./Arduino\ Codes/Blink/Blink.ino')
		os.system('stty -F /dev/ttyACM0 -hupcl')
		if request.POST['action_code'] == '0':
			os.system('echo "0" > /dev/ttyACM0')
		elif request.POST['action_code'] == '1':
			os.system('echo "1" > /dev/ttyACM0')
		elif request.POST['action_code'] == '2':
			os.system('echo "2" > /dev/ttyACM0')
	return render(request, 'arduino_controller/index.html', {})