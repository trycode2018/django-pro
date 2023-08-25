from django.urls import reverse

def test_status_code(client): 
    resposta = client.get('tarefas:home')
    assert resposta.status_code == 200
    #print('passou')