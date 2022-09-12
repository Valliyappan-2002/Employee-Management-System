from . import form
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import random as r
from . import models

sec_key = {}
def dispHome(req):
    return render(req, 'home.html', {'name':'VasanMeena'})


def adminFeat(req):
    if req.method == 'POST':
        emp = form.EmpLog(req.POST)
        if emp.is_valid():
            emp_id = emp.cleaned_data['emp_id']
            pswd = emp.cleaned_data['pswd']
            try:
                e = models.Employee.objects.get(pk = int(emp_id))
                print(e.pswd, pswd)
                if e.pswd != pswd:
                    return HttpResponse("Invalid password, try login again")
                if e.pos != 'Admin':
                    return HttpResponse("You don't have the rights")
            except Exception:
                return HttpResponse('Invalid id, try login again')
            num = r.randint(1000, 2000)
            sec_key.update( {str(emp_id): str(num)} )
            return HttpResponseRedirect('/vasanmeena/showEmps/' + str(emp_id) +'/'+str(num))
        else:
            return render(req, 'loginfrm.html', {'frm': emp})
            
    else:
        return render(req, 'loginfrm.html', {'dest': 'adminFeat/', 'frm': form.EmpLog(), 'eventName': 'Login'})


def showEmps(req, secnum, id):
    if sec_key[id] == secnum:
        emp = models.Employee.objects.all()[:10]
        return render(req, 'empDisp.html', {'dest':id+"/"+secnum+"/", 'empLst':emp, 'name':'VasanMeena'})
    else:
        return HttpResponse("Invalid")

sal_design ={
    'SDE': 60000,
    'ST': 50000,
    'DA': 65000
    }

def createEntry(req, secnum, id):
    if secnum == sec_key[id]:
        if req.method =="POST":
            e = form.EmpEntry(req.POST)
            if e.is_valid():
                e = e.save(commit= False)
                e.sal = sal_design[req.POST['design']]
                e.save()
                return HttpResponseRedirect('/vasanmeena/showEmps/'+id+'/'+secnum)
            else:
                return render(req, 'loginfrm.html', {'dest':'createEntry/'+id+"/"+secnum+"/", 'eventName': 'createEntry', 'frm': e})
        else:
            e = form.EmpEntry()
            return render(req, 'loginfrm.html', {'dest':'createEntry/'+id+"/"+secnum+"/", 'eventName': 'createEntry', 'frm': e})
    else:
        return HttpResponse("Invalid")
    

def update(req, eid, id, secnum):
    if sec_key[id] == secnum:
        e = models.Employee.objects.get(pk = int(eid))
        if req.method == 'POST':
            k = req.POST.copy()
            k.update({'id':eid, 'sal': sal_design[k['design']]})
            f = form.EmpEntry(k, instance = e)
            print(k)
            if f.is_valid():
                f.save()
                return HttpResponseRedirect('/vasanmeena/showEmps/'+id+'/'+secnum)
            else:
                return render(req, 'loginfrm.html', {'dest':'updateEntry/'+id+"/"+secnum+"/", 'eventName': 'updateEntry', 'frm': f})                
        else:
            frm = form.EmpUpFrm(initial = {'id': eid,'design': e.design, 'age': e.age, 'id':e.id, 'name':e.name, 'pos': e.pos, 'pswd': e.pswd})
            return render(req, 'loginfrm.html', {'dest':'update/'+eid+'/'+id+"/"+secnum+"/", 'eventName': 'updateEntry', 'frm': frm})
    else:
        return HttpResponse("Invalid, try login again")

def delete(req, eid, id, secnum):
    if sec_key[id] == secnum:
        e = models.Employee.objects.get(pk = int(eid))
        e.delete()
        return HttpResponseRedirect('/vasanmeena/showEmps/'+id+'/'+secnum)
    else:
        return HttpResponse("Invalid, try log in again")
    
def empFeat(req):
    if req.method == 'POST':
        try:
            e = models.Employee.objects.get(pk = int(req.POST['emp_id']))
            if e.pswd != req.POST['pswd']:
                return HttpResponse("Invalid credentials, try login again")
        except:
            return HttpResponse("Invalid credentials, try login again")        
        e = models.Employee.objects.all()[:15]
        return render(req, 'empDisp1.html', {'name':'VasanMeena', 'empLst':e})
    else:
        e = form.EmpLog()
        return render(req, 'loginfrm.html', {'eventName': 'Login', 'dest':'empFeat/', 'frm':e})


