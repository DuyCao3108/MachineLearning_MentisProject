from django.shortcuts import render
from django.http import HttpResponse
import pickle as pkl
import joblib
from joblib import dump, load
# model = load(r"C:\Users\Windows 10\mlproject\pkmodel" + ".pickle")
model = load('picklemodel.pickle2')
# def form(request):
#     if request.method == 'POST':
#             price = request.POST['price']
#             perception_usefullness = request.POST['perception_usefullness']
#             percetion_aesthetic = request.POST['percetion_aesthetic']
#             perception_trustworthy = request.POST['perception_trustworthy']
#             perception_relaxing = request.POST['perception_relaxing']
#             personality_extroversion = request.POST['personality_extroversion']
#             personality_neuroticism = request.POST['personality_neuroticism']
#             knowledge_importance = request.POST['knowledge_importance']
#             knowledge_otherapp = request.POST['knowledge_otherapp']
#             y_pred = model.predict([[price, perception_usefullness, percetion_aesthetic, 
#                                      perception_trustworthy,perception_relaxing,
#                                      personality_extroversion,personality_neuroticism,
#                                      knowledge_importance,knowledge_otherapp]])
#             if y_pred[0] == 0:
#                 y_pred = 'IS NOT Intended to pay'
#             else:
#                 y_pred = 'IS Intended to pay'
#             return render(request, 'test1.html', {'result' : y_pred})
#     return render(request, 'test1.html')

def results(request):
     if request.method == 'POST':
            price = request.POST['price']
            perception_usefullness = request.POST['perception_usefullness']
            percetion_aesthetic = request.POST['percetion_aesthetic']
            perception_trustworthy = request.POST['perception_trustworthy']
            perception_relaxing = request.POST['perception_relaxing']
            personality_extroversion = request.POST['personality_extroversion']
            personality_neuroticism = request.POST['personality_neuroticism']
            knowledge_importance = request.POST['knowledge_importance']
            knowledge_otherapp = request.POST['knowledge_otherapp']
            y_pred = model.predict([[price, perception_usefullness, percetion_aesthetic, 
                                     perception_trustworthy,perception_relaxing,
                                     personality_extroversion,personality_neuroticism,
                                     knowledge_importance,knowledge_otherapp]])
            if y_pred[0] == 0:
                y_pred = 'DOES NOT Intend to pay'
            else:
                y_pred = 'DOES Intend to pay'
            return render(request, 'results.html', {'result' : y_pred})
     

def form(request):
     return render(request, 'test1.html')
