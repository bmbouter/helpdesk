# Create your views here.
from django.shortcuts import render_to_response
from FIHelpSite.FISite.models import Page
from FIHelpSite.FISite.models import CifsShareModel
import re
		

def osType(request):
		OS=request.META['HTTP_USER_AGENT']
		print OS
		if (re.search("Macintosh;",OS)!=None):
			return render_to_response("fiMac.html",CifsShare.db)
		else:
			return render_to_response("fiPC.html",CifsShare.db)

#make a database call in your view
#load the share names into the db
#fetch them in the view
#pass the share names into the render complex
#1:46 PM
#then rewrite the template code so it loops through the share info retrieved from the database