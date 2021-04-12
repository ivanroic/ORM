from django.shortcuts import render, redirect

def count(request):
    if 'counter' in request.session:
        print('key exists!')
        request.session['counter'] = request.session['counter']+1
    else:
        request.session['counter'] = 0
        print("key 'counter' does NOT exist")
    return render(request, 'index.html')

def addTwo(request):
    if 'counter' in request.session:
        print('key exists!')
        request.session['counter'] = request.session['counter']+2
    else:
        request.session['counter'] = 0
        print("key 'counter' does NOT exist")
    return render(request, 'show.html')

def increment(request):
    # print("Got Post Info....................")
    # count_from_form = request.POST['count']
    # if 'counter' in request.session:
    #     print('key exists!')
    #     request.session['counter'] = request.session['counter'] + int(count_from_form)
    # else:
    #     request.session['counter'] = 0
    #     print("key 'counter' does NOT exist")

    num_from_form = request.POST['count']
    context = {
        "num_on_template" : num_from_form
    }
    return render(request,"show.html", context)

def destroy(request):
    del request.session['counter']
    return redirect("/root")