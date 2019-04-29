from django.shortcuts import render

# Create your views here.

def post_list(request):
	if request.method == "POST":
		print("Recieved POST")
		if request.POST['action_code'] == '0':
			print("LED Off")
		elif request.POST['action_code'] == '1':
			print("Start LED Blinking")
		elif request.POST['action_code'] == '2':
			print("LED On")
	return render(request, 'arduino_controller/index.html', {})