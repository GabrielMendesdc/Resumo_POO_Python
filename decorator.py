import time

def calcula_tempo(funcao):
    def wrapper():     
        tempo_comeco = time.time()
        funcao()
        tempo_final = time.time()
        print(f'sua função demorou {tempo_final - tempo_comeco}')
    return wrapper()


@calcula_tempo
def conta1000():
    for i in range(1000000):
        print(i)


