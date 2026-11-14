# correção da inclinação por rotação
from PIL import image

# gira a imagem pelo ângulo estimado, mantendo a página inteira.
def corrigir_inclinação (imagem: Image.Image, angulo: float) -> Image.Image:
    return imagem.rotate(
        angulo,
        resample = Image.Resampling.BICUBIC,
        expand = True, # aumenta a tela para não cortar os cantos
        fillcolor = "white",
    )