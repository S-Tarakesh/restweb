from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
    return render(request,"home.html",)
def AboutUs(request):
    return render(request,"AboutUs.html")
def contact(request):
    success = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        remark = request.POST.get("remark")

        if name and email and remark:
            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                remark=remark
            )
            success = True

    return render(request, "contact.html", {
        "success": success
    })
