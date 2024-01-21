from django.shortcuts import render, redirect

# Create your views here.





def test(request):

	return render(request, 'test.html')








def test2(request):

	 #if request.method == "POST":
        #query_name2 = request.POST.get('name', None)
    x = request.GET.get('op1')
    y = request.GET.get('op2')
    z = request.GET.get('op3')
    if x == '2' and y == '6' and z == '7':

        
        return render(request, 'test2.html')
    else:

    	return render(request, 'test3.html')

    

