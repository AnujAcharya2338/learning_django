from django.shortcuts import render

# Create your views here.
def recepies(request):
    if request.method == "POST":
        data = request.POST
        recepie_name = data.get('recepe_name')
        recepie_description = data.get('recepe_description')

        print(recepie_name)
        print(recepie_description)


        return render(request, 'recepies.html')