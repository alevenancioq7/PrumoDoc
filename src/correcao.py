#correção da inclinação por rotação
from PIL import image

#gira a imagem pelo ângulo estimado, mantendo a página inteira.
def corrigir_inclinação (imagem: image.image, angulo:float) ->image.image: 
    return imagem.rotate(
    angulo,
    resample = Image.Resampling.BICUBIC,
    expand = True
    fillcolor = "White"
    )