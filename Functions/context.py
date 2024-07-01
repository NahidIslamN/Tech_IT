from Functions.models import PublicMessage

def context_data(request):
    number = PublicMessage.objects.filter(seen_status = False).count()

    return{
        "number":number,
    }