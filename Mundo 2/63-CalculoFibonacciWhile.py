print(''' 
 |  ____||_   _||  _ \  / __ \ | \ | || \ | |    /\    / ____||_   _|
 | |__     | |  | |_) || |  | ||  \| ||  \| |   /  \  | |       | |  
 |  __|    | |  |  _ < | |  | || . ` || . ` |  / /\ \ | |       | |  
 | |      _| |_ | |_) || |__| || |\  || |\  | / ____ \| |____  _| |_ 
 |_|     |_____||____/  \____/ |_| \_||_| \_|/_/    \_\\_____||_____|
                                                                     
                                                                     ''')

termos = int(input('Quantos termos você quer ver? '))
c = 0
primeiro = 0
anterior = 1
novo = 0
while c < termos:
    print(primeiro, end=' ')
    novo = anterior + primeiro
    anterior = primeiro
    primeiro = novo
    c += 1
