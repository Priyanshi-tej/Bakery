from django.shortcuts import  render
from . import  pool
from django.contrib import auth

def UserLogin(request):
    return render(request,"UserLogin.html",{"msg":""})
def UserChkLogin(request):
     btn = request.POST['btn']

     if(btn=='Register'):
         return render(request, "UserRegister.html", {"msg": ""})

     else:
      userid = request.POST['userid']
      password = request.POST['password']

      db, cmd = pool.connection()
      query="select * from userregistration where userid='{0}' and password='{1}'".format(userid,password)

      cmd.execute(query)
      row=cmd.fetchone()
      if(row):
        query = "select * from shopping"
        cmd.execute(query)
        rows = cmd.fetchall()
        print(rows)

        return render(request, "Shopping.html", {'rows': rows})
      else:
        return render(request, "UserLogin.html", {"msg": "Invalid Userid/Password"})

def UserRegister(request):
    return render(request,"UserRegister.html",{"msg":""})
def UserRegisterNew(request):
 try:
     userid = request.POST['userid']
     username = request.POST['username']
     password = request.POST['password']
     db, cmd = pool.connection()
     q = "insert into userregistration(userid,username,password)values('{0}','{1}','{2}')" \
            .format(userid,username,password)


     print(q)
     cmd.execute(q)
     db.commit()
     db.close()

     return render(request, "UserRegister.html", {'msg': 'Record Submitted'})



 except Exception as e:
    print(e)

    return render(request, "UserRegister.html", {'msg': 'Fail To Submit Record'})

