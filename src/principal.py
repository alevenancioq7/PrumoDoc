import argparse
from PIL import Image, ImageOps, UnidentifiedImageError
from .correcao import corrigir_inclinacao
from .inclinacao import estimar_angulo

# define e lê os argumentos digitados no terminal
def ler_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description = "Corrige a inclinação de um documento digitalizado.")
    parser.add_argument("entrada", help = "caminho da imagem inclinada")
    parser.add_argument("-o", "--saida", default = "corrigida.png", help = "caminho da imagem corrigida")
    return parser.parse_args()

def main() -> None:
    argumentos = ler_argumentos()

    try:
        imagem = ImageOps.exif_transpose(Image.open(argumentos.entrada))
    except (FileNotFoundError, UnidentifiedImageError):
        raise SystemExit(f"Não foi possível abrir a imagem: {argumentos.entrada}")
    angulo = estimar_angulo(imagem)
    corrigir_inclinacao(imagem, angulo).save(argumentos.saida)
    print(f"Ângulo aplicado: {angulo:+.2f} graus. Salvo em {argumentos.saida}")

if __name__ == "__main__":
    main()