# estimativa do ângulo de inclinação de um documento
import numpy as np
from PIL import Image
from .gradiente import magnitude_gradiente

ANGULOS_TESTADOS = np.arage(-15, 15.25, 0.25)
LADO_MAXIMO = 800

# função objetivo para variância da soma dos pixels de cada linha
def variancia_projecao(bordas: Image.Image) -> float:

    # projeção horizontal
    projecao = np.asarray(bordas, dtype=float).sum(axis=1)
    return projecao.var()

# devolve o ângulo de inclinação do documento em graus
def estimar_angulo(imagem: Image.Image) -> float:

    # tons de cinza (cria uma cópia)
    reduzida = imagem.convert("L")

    # reduz mantendo a proporção
    reduzida.thumbnail((LADO_MAXIMO, LADO_MAXIMO))

    magnitude = magnitude_gradiente(np.asarray(reduzida))
    bordas = Image.fromarray(magnitude.astype(np.float32))

    pontuacoes = [
        variancia_projecao(bordas.rotate(angulo, resample=Image.Resampling.BILINEAR))
        for angulo in ANGULOS_TESTADOS
    ]
    return float(ANGULOS_TESTADOS[np.argmax(pontuacoes)])