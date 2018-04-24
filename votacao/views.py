from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Questao, Opcao
from votacao.models import Questao, Opcao
from django.template import loader
from django.urls import reverse
"""
def index(request):
    return HttpResponse("Hello,world. Esta e a pagina de entrada da app votacao.")

def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    output = ', '.join([q.questao_texto for q in latest_question_list])
    return HttpResponse(output)
"""
def index(request):
 latest_question_list = Questao.objects.order_by('-pub_data')[:5]
 latest_question_list = Questao.objects.order_by('-pub_data')[:5]
 context = {'latest_question_list': latest_question_list}
 return render(request, 'votacao/index.html', context)

def detalhe(request, questao_id):
 questao = get_object_or_404(Questao, pk=questao_id)
 return render(request, 'votacao/detalhe.html', {'questao': questao})

def resultados(request, questao_id):
 questao = get_object_or_404(Questao, pk=questao_id)
 return render(request, 'votacao/resultados.html', {'questao': questao})

def nova_questao(request):
    return render(request, 'votacao/nova_questao.html')

def nova_opcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/nova_opcao.html', {'questao': questao})

def gravar_novaquestao(request):
    try:
        text = request.POST['text']
        if text == "" or not text.endswith('?'):
            return render(request, 'votacao/nova_questao.html', {'error_message': "Não escreveu nenhuma questão!",})
    except (KeyError, Questao.DoesNotExist):
        return render(request, 'votacao/nova_questao.html', {'error_message': "Não escreveu nenhuma questão!",})
    else:
        q = Questao(questao_texto= text, pub_data=timezone.now())
        q.save()
        #latest_question_list = Questao.objects.order_by('-pub_data')[:5]
        #latest_question_list = Questao.objects.order_by('-pub_data')[:5]
        #context = {'latest_question_list': latest_question_list}
        #return render(request, 'votacao/index.html', context)
        return HttpResponseRedirect(reverse('votacao:index'))

def gravar_novaopcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        text = request.POST['opcao']
        if text == "":
            return render(request, 'votacao/nova_opcao.html', {'questao': questao, 'error_message': "Não escreveu nenhuma opção!", })
    except (KeyError, Opcao.DoesNotExist):
        return render(request, 'votacao/nova_opcao.html', {'questao': questao, 'error_message': "Não escreveu nenhuma opção!", })
    else:
        questao.opcao_set.create(opcao_texto = text, votos=0)
        #return render(request, 'votacao/detalhe.html', {'questao': questao })
        return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))

def apagar_questao(request):
    list = Questao.objects.order_by('-pub_data')
    context = {'list': list}
    return render(request, 'votacao/apagar_questao.html', context)

def opcao_a_apagar(request):
    list = Questao.objects.order_by('-pub_data')
    try:
        questao = Questao.objects.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        return render(request, 'votacao/apagar_questao.html', {'list': list, 'error_message': "Não escolheu nenhuma questão para ser eliminada!", })
    else:
        questao.delete()
        #latest_question_list = Questao.objects.order_by('-pub_data')[:5]
        #latest_question_list = Questao.objects.order_by('-pub_data')[:5]
        #context = {'latest_question_list': latest_question_list}
        #return render(request, 'votacao/index.html', context)
        return HttpResponseRedirect(reverse('votacao:index'))


def voto(request, questao_id):
 questao = get_object_or_404(Questao, pk=questao_id)
 try:
    opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
 except (KeyError, Opcao.DoesNotExist):
 # Apresenta de novo o form para votar
    return render(request, 'votacao/detalhe.html', {'questao': questao, 'error_message': "Não escolheu uma opção",})
 else:
    opcao_seleccionada.votos += 1
    opcao_seleccionada.save()
 # Retorne sempre HttpResponseRedirect depois de
 # tratar os dados POST de um form
 # pois isso impede os dados de serem tratados
 # repetidamente se o utilizador
 # voltar para a página web anterior.
    return HttpResponseRedirect(reverse('votacao:resultados',args=(questao.id,)))
