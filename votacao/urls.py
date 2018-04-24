from django.conf.urls import url
from . import views
# (. significa que importa views da mesma directoria)

app_name = 'votacao'
urlpatterns = [
 # ex: /votacao/
 url(r'^$', views.index, name='index'),
 # ex: /votacao/5/
 url(r'^(?P<questao_id>[0-9]+)/$', views.detalhe, name='detalhe'),
 # ex: /votacao/5/resultados/
 url(r'^(?P<questao_id>[0-9]+)/resultados/$', views.resultados, name='resultados'),
 # ex: /votacao/5/voto/
 url(r'^(?P<questao_id>[0-9]+)/voto/$', views.voto, name='voto'),
 url(r'nova_questao/$', views.nova_questao, name='nova_questao'),
 url(r'gravar_novaquestao/$', views.gravar_novaquestao, name='gravar_novaquestao'),
 url(r'^(?P<questao_id>[0-9]+)/nova_opcao/$', views.nova_opcao,name='nova_opcao'),
 url(r'^(?P<questao_id>[0-9]+)/gravar_novaopcao/$', views.gravar_novaopcao, name='gravar_novaopcao'),
 url(r'apagar_questao/$', views.apagar_questao, name='apagar_questao'),
url(r'opcao_a_apagar/$', views.opcao_a_apagar, name='opcao_a_apagar'),
]