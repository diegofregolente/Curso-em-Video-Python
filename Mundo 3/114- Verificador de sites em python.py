import urllib.request

site = str(input('Digite uma URL: ')).strip()

try:
    urllib.request.urlopen(f"http://{site}").getcode()
    urllib.request.urlopen(f"https://{site}").getcode()
except:
    print('\033[0:31mNão conseguir acessar o site do Pudim.') # if getcode() != 200-299
else:
    print('\033[0:32mConsegui acessar o site do Pudim.') # if getcode() = 200-299

# Respostas de informação (100-199)
# Respostas de sucesso (200-299) - OK
# Redirecionamentos (300-399)
# Erros do cliente (400-499) -
# Erros do servidor (500-599)