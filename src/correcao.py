# correção da inclinação por rotação
from PIL import Image

# gira a imagem pelo ângulo estimado, mantendo a página inteira
def corrigir_inclinacao(imagem: Image.Image, angulo: float) -> Image.Image:
    return imagem.rotate(
        angulo,
        resample = Image.Resampling.BICUBIC, #interpolação suave
        expand = True, # aumenta a tela para não cortar os cantos
        fillcolor = "white", # cantos novos ficam brancos
    )