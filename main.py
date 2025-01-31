from carro_inteligente import CarroInteligente
from carro_esportivo import CarroEsportivo
from carro_corrida import CarroCorrida

def test_drive(carro):
    print(f"\nTestando (carro.__class__.__name__):")
    carro.acelera()
    carro.exibe_velocidade()

if __name__ == "__main__":
    # Testandp CarroInteligente
    carro_inteligente = CarroInteligente(10)
    print("Carro inteligente:")
    carro_inteligente.acelera()
    carro_inteligente.exibe_velocidade()
    carro_inteligente.estaciona()
    print()

    # Testando CarroEsportivo
    carro_esportivo = CarroEsportivo(50)
    print("Carro esportivo:")
    carro_esportivo.turbo()
    carro_esportivo.exibe_velocidade()
    carro_esportivo.freia()
    carro_esportivo.exibe_velocidade()

    #Testando CarroCorrida
    carro_corrida = CarroCorrida(100)
    test_drive(carro_corrida)



