from django.shortcuts import render

def appmain(request):
	d = {
		'your_blood': request.GET.get('your_blood'),
		'his_blood': request.GET.get('his_blood')
    }
	yours = d['your_blood']
	his = d['his_blood']
	print(yours)
	print(his)
	if yours == '1' and his == '1':
		return render(request, 'appname/a_a.html',d)
	elif yours == '1' and his == '2':
		return render(request, 'appname/a_b.html',d)
	elif yours == '1' and his == '3':
		return render(request, 'appname/a_o.html',d)
	elif yours == '1' and his == '4':
		return render(request, 'appname/a_ab.html',d)
	elif yours == '2' and his == '1':
		return render(request, 'appname/a_b.html',d)
	elif yours == '2' and his == '2':
		return render(request, 'appname/b_b.html',d)
	elif yours == '2' and his == '3':
		return render(request, 'appname/b_o.html',d)
	elif yours == '2' and his == '4':
		return render(request, 'appname/b_ab.html',d)
	elif yours == '3' and his == '1':
		return render(request, 'appname/a_o.html',d)
	elif yours == '3' and his == '2':
		return render(request, 'appname/b_o.html',d)
	elif yours == '3' and his == '3':
		return render(request, 'appname/o_o.html',d)
	elif yours == '3' and his == '4':
		return render(request, 'appname/o_ab.html',d)
	elif yours == '4' and his == '1':
		return render(request, 'appname/a_ab.html',d)
	elif yours == '4' and his == '2':
		return render(request, 'appname/b_ab.html',d)
	elif yours == '4' and his == '3':
		return render(request, 'appname/o_ab.html',d)
	elif yours == '4' and his == '4':
		return render(request, 'appname/ab_ab.html',d)
	else:
		return render(request, 'appname/uranai.html',d)
