import numpy as np
import pytest
from PIL import Image
from src.correcao import corrigir_inclinação
from src.inclinacao import estimar_inclinacao

# página branca com "linha de texto" (faixas pretas) horizontais
def criar_documento() -> Image.Image:
    pagina = np.full((400, 600), 255, dtype=np.uint8)
    linhas = (np.arange(400) % 30) < 6 #6 pixels pretos a cada 30
    pagina[linhas, 50:550] = 0
    return Image.fromarray(pagina)

#teste que estima o ângulo de correção do documento
@pytest.mark.parametrize("inclinacao", [-10, -3, 5, 12])
def teste_estima_correcao(inclinacao):
    inclinada = criar_documento().rotate(inclinacao, fillcolor= "White")
    assert estimar_angulo(inclinada) == pytest.approx(-inclinacao, abs=1)

#teste para verificar se o documento reto tem ângulo zero
def teste_documento_angulo():
    assert estimar_angulo(criar_documento()) == pytest.approx(0, abs = 0.5)

#teste de correção para deixar o documento alinhado
def teste_correcao_documento():
    inclinada = criar_documento().rotate(8, fillcolor= "White")
    corrigida = corrigir_inclinacao(inclinada, estimar_angulo(inclinada))
    assert estimar_angulo(corrigida) == pytest.approx(0, abs = 1)