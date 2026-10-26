# derivadas parciais e gradiente da imagem
import numpy as np

# calcula |grad f| = raiz((df/dx)^2 + (df/dy)^2) em cada pixel
def magnitude_gradiente(cinza: np.ndarray) -> np.ndarray:

    # eixo 0 = y, eixo 1 = x
    df_dy, df_dx = np.gradient(cinza.astype(float))
    return np.hypot(df_dx, df_dy) #raiz da soma dos quadrados