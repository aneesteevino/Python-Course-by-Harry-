# A Python Virtual Environment is an isolated space 
# where you can work on your Python projects, separately from your system-installed Python.
# You can set up your own libraries and dependencies without affecting the system Python.

# A Python Virtual Environment is like a private room 
# for each of your Python projects.
#  It keeps all the tools and stuff (like libraries and dependencies) 
# your project needs separate from your computer's main Python setup. 
# This way, each project stays tidy and doesn't mess with the others.\


# python virtual enviroment 
# iss mai hum apna python interpreter banatay hain ya phr esa keh skty hn k apna new born python bnaegy
# jis mai hum apni mrzi ki dependencies set krskty hn or apni mrzi ki libraries add krskty hain
# python virtual enviroment bnany k liye humain pehly python ka virtual enviroment install krna hota hai
# (python -m venv myenv) sy virtual enviroment bna skty hain cmd mai
 
# python virtual envirornment ki zaroorat kyun parti hai?
# jab hum kisi project pr kaam krty hain to us project k liye humain kuch libraries or dependencies install krni parti hain
# ya phr kbhi kbhi esa hota hai k apny ek client ko python 3.8 mai project bana k dia hai or uss client k pass python 3.6 hai
# to uss client k pass project run nhi hoga


# virtual enviroment basically clone hota hai hamaary acctual python ka 
# hum jitny mrzi k python bnaa skty hain 

# Example of virtual environment
# let suppose you are working on (A,B) projects where project A requires flask version 2.1 
# on another hand project B requires flask version 2.3 however you can not have both versions installed in a globally python version at a time
# so they will conflict eachother 
# to avoid this conflict we make virtual enviroment


# how to create virtual enviroment??????

# (python -m venv myenv) sy virtual enviroment bna skty hain cmd mai 
# myenv ek folder hai jo k hamary project k sath create ho jata hai

# (myenv\Scripts\activate) sy virtual enviroment ko activate kr skty hain
# activate krny k baad (pip list) sy dekh skty hain k virtual enviroment mai kon kon sy libraries install hain

# (deactivate) sy virtual enviroment ko deactivate kr skty hain

# we use pip freeze to save all the libraries in a file or view all the libraries in a file

# agr ap apna project kisi or system pr run krwana chahty hain to apko apny project k sath requirements.txt file bhi share krni parti hai
# jis sy dosry tsystem pr apny libraries install kr skty hain
# (pip freeze > requirements.txt) sy libraries ko save kr skty hain or requirements name sy ek file bnega jisme sary packages k naam or versions hongy jo k mai current virtual enviroment mai use kr rha honga



# (pip install -r requirements.txt) sy libraries ko install kr skty hain jo k requirements.txt file mai hain
# example : agr ap ye project kisi dost ko dena chahta hain to wo mery requirement.txt waly packages ko apny system mai install kr skta hai
