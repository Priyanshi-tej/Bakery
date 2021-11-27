from django.shortcuts import  render
from . import  pool
from django.contrib import auth
def ProductInterface(request):
    return render(request, "Product.html", {'msg': ""})



def ProductSubmit(request):
 try:
    btn = request.POST['btn']
    pname = request.POST['pname']
    i1 = request.POST['i1']
    q1 = request.POST['q1']
    i2 = request.POST['i2']
    q2 = request.POST['q2']
    i3 = request.POST['i3']
    q3 = request.POST['q3']
    i4 = request.POST['i4']
    q4 = request.POST['q4']


    if (btn == 'Logout'):
        return render(request, "AdminLogin.html", {'msg': ""})
    elif (btn=='Submit'):
        db, cmd = pool.connection()
        q = "insert into product(productname,Ig1,Q1,Ig2,Q2,Ig3,Q3,Ig4,Q4)values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')" \
            .format(pname, i1, q1, i2, q2, i3, q3, i4, q4)


        print(q)
        cmd.execute(q)
        db.commit()
        db.close()

        return render(request, "Product.html", {'msg': 'Record Submitted'})



 except Exception as e:
    print(e)

    return render(request, "Product.html", {'msg': 'Fail To Submit Record'})
def ProductDisplay(request):
    try:
        db, cmd = pool.connection()
        query = "select * from product"
        cmd.execute(query)
        rows=cmd.fetchall()
        print(rows)
        return render(request,"ProductDisplay.html",{'rows': rows})
    except Exception as e:
        return render(request, "ProductDisplay.html", {'rows': []})
def Logout(request):
    try:
        btn = request.POST['btn']
        if(btn=='Logout'):



         return render(request,"AdminLogin.html",{'msg': ""})

    except Exception as e:
            return render(request, "AdminLogin.html", {'rows': []})



