from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
# 	return HttpResponse('''<h1>ekman singh</h1> <h2><a
# 	href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django website</a></h2>''')
# def about(request):
# 	return HttpResponse("hello to me.")

def index(request):
	# d = {"name":"ekman","place":"USA"}
	return render(request, "index.html")#,d
	# return HttpResponse("Home")
#
# def removepunc(request):
# 	djtext = "\n" + request.GET.get('text','default')
#
# 	return HttpResponse("remove punc")
#
# def capfirst(request):
# 	return HttpResponse("capitalize first")
#
# def newlineremove(request):
# 	return HttpResponse("new line remove")
#
# def spaceremove(request):
# 	return HttpResponse("space remover")
#
# def charcount(request):
# 	return HttpResponse("charcount")

def analyze(request):
	djtext = request.POST.get('text','default')
	removepunc = request.POST.get('removepunc','off')
	fullcaps = request.POST.get('fullcaps','off')
	newlineremover = request.POST.get('newlineremover','off')
	extraspaceremover = request.POST.get('extraspaceremover','off')
	charcount = request.POST.get('charcount','off')
	if removepunc == "on":
		punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
		analyzed = ""
		for char in djtext:
			if char not in punctuation:
				analyzed = analyzed + char
		params = {"purpose":"Remove Punctuation","analyzed_text":analyzed}
		djtext = analyzed
		# return render(request,"analyze.html",params)
	if fullcaps == "on":
		analyzed = ""
		for char in djtext:
			analyzed = analyzed + char.upper()
		params = {"purpose":"Changed to Uppercase","analyzed_text":analyzed}
		djtext = analyzed
		# return render(request,"analyze.html",params)
	if newlineremover == "on":
		analyzed = ""
		for char in djtext:
			if char != "\n" and char != "\r":
				analyzed = analyzed + char
		params = {"purpose":"Remove New Lines","analyzed_text":analyzed}
		djtext  = analyzed
		# return render(request,"analyze.html",params)
	if extraspaceremover == "on":
		analyzed = ""
		for indexs, char in enumerate(djtext):
			if not (djtext[indexs] == " " and djtext[indexs+1] == " "):
				analyzed = analyzed + char
		params = {"purpose":"Extra spaces remover","analyzed_text":analyzed}
		djtext = analyzed
		# return render(request,"analyze.html",params)
	if charcount == "on":
		ek = len(djtext)
		analyzed = f"The lenght of text that you have Enter is {ek}."
		params = {"purpose":"Charater Count","analyzed_text":analyzed}
	
	if removepunc != "on" and newlineremover != "on" and fullcaps != "on" and extraspaceremover != "on" and charcount != "on":
		return HttpResponse("Error!")
	
	
	return render(request,"analyze.html",params)