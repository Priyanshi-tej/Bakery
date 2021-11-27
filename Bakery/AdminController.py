from django.shortcuts import  render
from . import  pool
from django.contrib import auth

def AdminLogin(request):
    return render(request,"AdminLogin.html",{"msg":""})
def AdminChkLogin(request):
     btn = request.POST['btn']

     if(btn=='Register'):
         return render(request, "Register.html", {"msg": ""})

     else:
      adminid = request.POST['adminid']
      password = request.POST['password']

      db, cmd = pool.connection()
      query="select * from adminlogin where adminid='{0}' and password='{1}'".format(adminid,password)

      cmd.execute(query)
      row=cmd.fetchone()
      if(row):

        return render(request, "Product.html", {'msg': ""})
      else:
        return render(request, "AdminLogin.html", {"msg": "Invalid Adminid/Password"})

def Register(request):
    return render(request,"Register.html",{"msg":""})
def RegisterNew(request):
 try:
     adminid = request.POST['adminid']
     adminname = request.POST['adminname']
     password = request.POST['password']
     db, cmd = pool.connection()
     q = "insert into adminlogin(adminid,adminname,password)values('{0}','{1}','{2}')" \
            .format(adminid,adminname,password)


     print(q)
     cmd.execute(q)
     db.commit()
     db.close()

     return render(request, "Register.html", {'msg': 'Record Submitted'})



 except Exception as e:
    print(e)

    return render(request, "Register.html", {'msg': 'Fail To Submit Record'})

