import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Simulação de Daltonismo", layout="wide")


st.markdown(
    f"<h1 style='color: #0E0E52; text-align: center;'>Simulação de Daltonismo em Imagens</h1><h3 style='text-align: center;'>Este aplicativo foi desenvolvido como um tutorial interativo para demonstrar como simulações de daltonismo funcionam em imagens digitais.</h3>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style='text-align: center;'>
        <p>Gabriella Silveira Braz - 10402554</p>
        <p>Giovana Liao - 10402264</p>
        <p>Maria Julia de Pádua - 10400630</p>
    </div>
""",
    unsafe_allow_html=True,
)

# --- PARTE TEÓRICA ---

st.markdown(
    f"<div><h2 style='color: #192BC2;'>Parte Teórica</h2></div>",
    unsafe_allow_html=True,
)


# Texto HTML explicativo com estilos
st.markdown(
    """
<div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">

  <h3 style="color: #0072B2;">O que é Daltonismo?</h3>
  <p>
    O <strong>daltonismo</strong> é uma condição visual caracterizada pela dificuldade ou incapacidade de perceber certas cores corretamente.
    A causa está, em grande parte, em <strong>alterações genéticas</strong> que afetam os <em>fotorreceptores da retina</em> conhecidos como <em>cones</em>.
  </p>

  <h4 style="color: #0072B2;">Como vemos as cores?</h4>
  <p>O olho humano saudável possui três tipos principais de cones:</p>
  <ul>
    <li><strong>L-Cones</strong>: sensíveis à luz <strong style="color: red;">vermelha</strong></li>
    <li><strong>M-Cones</strong>: sensíveis à luz <strong style="color: green;">verde</strong></li>
    <li><strong>S-Cones</strong>: sensíveis à luz <strong style="color: blue;">azul</strong></li>
  </ul>
  <p>
    A percepção de cor ocorre pela combinação da ativação desses cones. Por exemplo, a cor amarela é percebida quando os cones vermelhos e verdes são ativados simultaneamente.
  </p>

  <h4 style="color: #0072B2;">Como o Daltonismo afeta a visão?</h4>
  <p>Em pessoas daltônicas, um ou mais desses cones estão ausentes ou funcionam de forma diferente, resultando em:</p>
  <ul>
    <li><strong>Protanopia</strong>: Falta ou disfunção dos cones vermelhos (L-Cones). Tons vermelhos parecem escuros ou marrons.</li>
    <li><strong>Deuteranopia</strong>: Falta ou disfunção dos cones verdes (M-Cones). Difícil distinguir entre vermelho e verde.</li>
    <li><strong>Tritanopia</strong>: Ausência de cones azuis (S-Cones). Azul e verde se confundem, amarelos podem desaparecer.</li>
  </ul>

  <p>Essas alterações impactam diretamente o modo como as cores são percebidas no dia a dia, afetando atividades como ler mapas coloridos, interpretar sinais de trânsito, e mais.</p>

  <h4 style="color: #0072B2;">Como simular o Daltonismo?</h4>
  <p>
    Para simular a visão de uma pessoa daltônica em uma imagem, usamos <strong>modelos matemáticos</strong> que modificam a forma como as cores aparecem.
  </p>
  <p>
    O processo se baseia em <strong>matrizes de transformação</strong> — cada tipo de daltonismo tem uma matriz que altera os valores RGB da imagem original.
  </p>
</div>
""",
    unsafe_allow_html=True,
)

# Etapa 1
st.markdown(
    '<h4 style="color: #0072B2;">Como funciona a simulação? (Passo a Passo com Código)</h4>',
    unsafe_allow_html=True,
)
st.markdown("#### Etapa 1: Carregar a imagem")
st.code(
    """
from PIL import Image
import numpy as np

# Abrir a imagem e converter para RGB
imagem = Image.open("exemplo.jpg").convert("RGB")
""",
    language="python",
)

# Etapa 2
st.markdown("#### Etapa 2: Converter a imagem para array NumPy normalizado")
st.code(
    """
# Converter a imagem para um array e normalizar os valores de 0 a 1
imagem_np = np.array(imagem).astype(float) / 255.0
""",
    language="python",
)

# Etapa 3
st.markdown("#### Etapa 3: Selecionar a matriz de simulação de Daltonismo")
st.markdown("Cada tipo de daltonismo tem sua própria matriz. Exemplo para Protanopia:")
st.code(
    """
# Matriz de transformação para Protanopia
matriz_protanopia = np.array([
    [0.56667, 0.43333, 0],
    [0.55833, 0.44167, 0],
    [0,       0.24167, 0.75833]
])
""",
    language="python",
)

# Etapa 4
st.markdown("#### Etapa 4: Aplicar a matriz aos pixels")
st.markdown(
    "Aqui ocorre a mágica: transformamos cada pixel da imagem multiplicando pelo modelo."
)
st.code(
    """
# Aplicar a matriz de simulação a cada pixel
imagem_simulada = imagem_np @ matriz_protanopia.T
""",
    language="python",
)

st.markdown("Exemplo de cálculo:")
st.code(
    """
R_sim = 0.56667*0.8 + 0.43333*0.6 + 0*0.2
G_sim = 0.55833*0.8 + 0.44167*0.6 + 0*0.2
B_sim = 0*0.8 + 0.24167*0.6 + 0.75833*0.2
""",
    language="python",
)

# Etapa 5
st.markdown("#### Etapa 5: Garantir que os valores estejam no intervalo [0,1]")
st.code(
    """
# Corrigir valores fora do intervalo
imagem_simulada = np.clip(imagem_simulada, 0, 1)
""",
    language="python",
)

# Etapa 6
st.markdown("#### Etapa 6: Converter para imagem novamente")
st.code(
    """
# Reescalar de volta para [0, 255] e converter para imagem
imagem_resultado = (imagem_simulada * 255).astype(np.uint8)
imagem_resultado = Image.fromarray(imagem_resultado)
""",
    language="python",
)

# Conclusão
st.markdown(
    '<h4 style="color: #0072B2;">Exemplo visual da transformação</h4>',
    unsafe_allow_html=True,
)
st.markdown(
    """
Se o pixel original era um tom de vermelho puro `[255, 0, 0]`, a simulação para **Protanopia** pode transformá-lo em marrom ou cinza,
pois os receptores para vermelho estão comprometidos.
"""
)

st.markdown(
    '<h4 style="color: #0072B2;">Por que isso é útil?</h4>', unsafe_allow_html=True
)
st.markdown(
    """
- **Design acessível**: Criar interfaces e sites mais amigáveis para pessoas com daltonismo.  
- **Educação e conscientização**: Permitir que pessoas sem deficiência visual entendam como o mundo pode parecer para daltônicos.  
- **Teste de acessibilidade automática**: Aplicar a simulação em interfaces para garantir distinção suficiente entre cores.
"""
)


st.markdown("---")

st.markdown(
    f"<div><h2 style='color: #192BC2;'>Simulação Prática</h2></div>",
    unsafe_allow_html=True,
)

st.subheader("1. Faça o upload de uma imagem:")
uploaded_file = st.file_uploader(
    "Escolha uma imagem no formato JPG ou PNG", type=["jpg", "jpeg", "png"]
)

st.subheader("2. Selecione o tipo de Daltonismo a simular:")
daltonism_type = st.selectbox(
    "2. Selecione o tipo de Daltonismo a simular:",
    ["Deuteranopia (verde)", "Protanopia (vermelho)", "Tritanopia (azul)"],
    label_visibility="collapsed",
)

# MATRIZES DE SIMULAÇÃO
MATRIZES = {
    "Protanopia (vermelho)": np.array(
        [[0.56667, 0.43333, 0], [0.55833, 0.44167, 0], [0, 0.24167, 0.75833]]
    ),
    "Deuteranopia (verde)": np.array([[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.3, 0.7]]),
    "Tritanopia (azul)": np.array(
        [[0.95, 0.05, 0], [0, 0.43333, 0.56667], [0, 0.475, 0.525]]
    ),
}


# --- FUNÇÃO DE SIMULAÇÃO ---
def simular_daltonismo(imagem, tipo):
    imagem_np = np.array(imagem).astype(float) / 255.0
    matriz = MATRIZES[tipo]

    resultado = imagem_np @ matriz.T
    resultado = np.clip(resultado, 0, 1)
    resultado = (resultado * 255).astype(np.uint8)

    return Image.fromarray(resultado)


# --- PROCESSAMENTO E RESULTADO ---
if uploaded_file:
    imagem_original = Image.open(uploaded_file).convert("RGB")

    st.subheader("3. visualize o resultado da simulação")
    cols = st.columns(2, gap="small")

    with cols[0]:
        st.image(imagem_original, caption="Imagem Original", width=350)

    imagem_simulada = simular_daltonismo(imagem_original, daltonism_type)

    with cols[1]:
        st.image(imagem_simulada, caption=f"Simulação: {daltonism_type}", width=350)

    with st.expander("📄 Código-Fonte Explicado", expanded=False):
        st.code(
            '''
from PIL import Image
import numpy as np

# Matrizes de simulação para diferentes tipos de daltonismo
MATRIZES = {
    "protanopia": np.array([
        [0.56667, 0.43333, 0],
        [0.55833, 0.44167, 0],
        [0,       0.24167, 0.75833]
    ]),
    "deuteranopia": np.array([
        [0.625, 0.375, 0],
        [0.7,   0.3,   0],
        [0,     0.3,   0.7]
    ]),
    "tritanopia": np.array([
        [0.95,   0.05,     0],
        [0,      0.43333,  0.56667],
        [0,      0.475,    0.525]
    ])
}

def simular_daltonismo(imagem_pil, tipo):
    """
    Aplica uma simulação de daltonismo à imagem fornecida.
    
    Args:
        imagem_pil: Objeto PIL.Image
        tipo: str, um dos ["protanopia", "deuteranopia", "tritanopia"]
    
    Returns:
        PIL.Image: imagem resultante com a simulação aplicada.
    """
    if tipo not in MATRIZES:
        raise ValueError(f"Tipo '{tipo}' inválido. Use: {list(MATRIZES.keys())}")

    # Conversão da imagem para numpy e normalização
    imagem_np = np.array(imagem_pil).astype(float) / 255.0

    # Seleção da matriz de transformação
    matriz = MATRIZES[tipo]

    # Aplicação da matriz de simulação (multiplicação matricial)
    resultado = imagem_np @ matriz.T

    # Garantia de valores válidos [0,1]
    resultado = np.clip(resultado, 0, 1)

    # Reescala para [0,255] e conversão para uint8
    resultado = (resultado * 255).astype(np.uint8)
    
    return Image.fromarray(resultado)

# Exemplo de uso
if __name__ == "__main__":
    # Abrir imagem original
    imagem = Image.open("exemplo.jpg").convert("RGB")

    # Tipo de daltonismo a simular
    tipo_daltonismo = "protanopia"  # ou "deuteranopia", "tritanopia"

    # Aplicar simulação
    imagem_simulada = simular_daltonismo(imagem, tipo_daltonismo)

    # Mostrar imagem original e simulada
    imagem.show(title="Original")
    imagem_simulada.show(title=f"Simulação: {tipo_daltonismo}")
    
    # Salvar se quiser
    # imagem_simulada.save(f"simulado_{tipo_daltonismo}.png")
''',
            language="python",
        )

    st.success("✅ Simulação concluída com sucesso!")


st.markdown("---")
st.markdown(
    f"<div><h2 style='color: #192BC2;'>Referências Bibliográficas</h2></div>",
    unsafe_allow_html=True,
)

st.markdown(
    """
- Machado, G. M., Oliveira, M. M., & Fernandes, L. A. (2009). A physiologically-based model for simulation of color vision deficiency. *IEEE Transactions on Visualization and Computer Graphics*, 15(6), 1291–1298.
- [Color Blindness Simulation Tool – Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/)
- Wikipedia: [Color Blindness](https://en.wikipedia.org/wiki/Color_blindness)
"""
)
