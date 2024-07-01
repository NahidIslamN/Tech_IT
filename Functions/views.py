from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from django.shortcuts import get_object_or_404

# Create your views here.
from django.views import View


from Functions.models import *





class HomePage(View):
    def get(self, request):
        return render(request,"index.html")
    

class AboutPage(View):
    def get(self,request):
        return render(request,"aboutus/about.html")
    
class LearnmoreAboutpage(View):
    def get(self,request):
        return render(request,"aboutus/learnmore.html")
    

class ServicePage(View):
    def get(self, request):
        service = Services.objects.filter(status = True)


        cp =  {
            'services':service
        }
        return render(request,'service/service.html', context=cp)
    
class learnMore(View):
    def get(self, request):
        my_id = request.GET.get('service_id')
        item = Services.objects.get(id = my_id)
        cp = {
            'service': item,
        }

        return render(request, 'service/learnmore.html', context=cp)

class TeamPage(View):
    def get(self, request):
        teamember = TeamMember.objects.filter(status = True)



        cp = {
            "teamember":teamember
        }
        return render(request,'team/team.html', context=cp)
    

class OurPortfolio(View):
    def get(self, request):
        portfolio = Portflolio_Projecrs.objects.all()


        cp = {
            "portfolio":portfolio,
        }
        return render(request,'portfolio/portfolio.html', context=cp)
    

class Pricings(View):
    def get(self, request):
        prices = Pricing.objects.all()

        cp = {
            "prices":prices,
        }
        return render(request,'pricing/pricing.html', context = cp)
    


class ContactUs(View):
    
    def get(self, request):

        return render(request,'contuct_us/contuct_us.html')
    
    def post(self, request):
        data = request.POST

        mgs = PublicMessage.objects.create(

            Name = data.get('name'),
            Email = data.get('email'),
            Subject = data.get('subject'),
            Message = data.get('message'),           

        )
        mgs.save() 
        messages.info(request,"Your message has been sent. Thank you!")
        return render(request,'contuct_us/contuct_us.html')


class PublicMessages(View):
    @method_decorator(login_required)
    def get(self, request):
        mgses = PublicMessage.objects.filter(seen_status = False)
        for i in mgses:
            i.seen_status = True
            i.save()
        
        all_mgs = PublicMessage.objects.all().order_by('-created_at')


        cp = {
            "all_mgs":all_mgs
        }
        return render(request,"inbox/messages.html", context=cp)
   








    

    




    



