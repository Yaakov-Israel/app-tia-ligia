import streamlit as st
import random # Vamos usar para sortear as palavras do nosso jogo!

# Configurações da página (é bom colocar no começo)
st.set_page_config(page_title="App da Tia Lígia", page_icon="📚", layout="wide")

# --- NOSSO MENU SECRETO NA LATERAL (SIDEBAR) ---
st.sidebar.title("🎒 Cantinho da Descoberta 🎒")
st.sidebar.markdown("---")
st.sidebar.image("https://img.freepik.com/vetores-gratis/menina-bonita-crianca-feliz-dos-desenhos-animados-com-livro_701961-2227.jpg?t=st=1716345038~exp=1716348638~hmac=2e3924f57d1252306177a3c68e72222cd8f160a0e2437e0e84808894ab8db76e&w=740", width=150) # Você pode trocar este link de imagem depois!
st.sidebar.markdown("---")

lista_de_aventuras = [
    "🌟 Página Inicial",
    "🔡 Português Divertido",
    "🔢 Matemática Mágica",
    "🌳 Mundo das Ciências",
    "📜 Viagem pela História do Brasil"
]
escolha_da_crianca = st.sidebar.selectbox("O que vamos explorar hoje, meu bem?", lista_de_aventuras)

# --- CONTEÚDO QUE APARECE NA PÁGINA PRINCIPAL ---

if escolha_da_crianca == "🌟 Página Inicial":
    st.title("✨ Bem-vindo(a) de volta ao App da Tia Lígia! ✨")
    st.subheader("Eu sou a Tia Lígia, sua Super-Professora, pronta para novas aventuras!")
    st.write("Explore o 'Cantinho da Descoberta' aqui do lado 👈 para escolher uma matéria e começar a diversão!")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://img.freepik.com/vetores-gratis/professora-explicando-na-sala-de-aula-com-estudantes_23-2148490575.jpg?t=st=1716345250~exp=1716348850~hmac=a63c7903422502202a13d5375e9a2745dbb0b2f5c49cc8a348b67098ccb3391e&w=1060", caption="Vamos aprender juntos!") # Você pode trocar este link de imagem depois!
    with col2:
        st.markdown("### O que você vai encontrar aqui?")
        st.markdown("""
        - Jogos e desafios de Português! 🔡
        - Quebra-cabeças de Matemática! 🔢
        - Descobertas incríveis em Ciências! 🌳
        - Aventuras pela História do nosso Brasil! 📜
        - E muito mais no futuro!
        """)
    st.balloons()

elif escolha_da_crianca == "🔡 Português Divertido":
    st.title("🔡 Aventura no Mundo das Palavras!")
    st.image("https://img.freepik.com/vetores-gratis/desenhos-animados-de-volta-ao-design-da-escola-com-material-escolar_23-2148588951.jpg?t=st=1716345436~exp=1716349036~hmac=b33a7d544254258679109396a1f848a7d5d29ffdbf6a18b262b019f7bc40505f&w=1060", width=300) # Você pode trocar este link de imagem depois!
    st.write("Olá, pequeno(a) escritor(a)! Vamos brincar com letras e palavras!")
    st.markdown("---")

    st.subheader("🎉 Jogo: Descubra a Letra Perdida! 🎉")

    palavras_do_jogo = {
        "CA_A": {"letra_certa": "S", "opcoes": ["S", "P", "L"], "palavra_completa": "CASA"},
        "GA_O": {"letra_certa": "T", "opcoes": ["M", "T", "R"], "palavra_completa": "GATO"},
        "BO_A": {"letra_certa": "L", "opcoes": ["N", "P", "L"], "palavra_completa": "BOLA"},
        "MA_Ā": {"letra_certa": "Ç", "opcoes": ["S", "X", "Ç"], "palavra_completa": "MAÇÃ"},
        "LU_A": {"letra_certa": "V", "opcoes": ["B", "F", "V"], "palavra_completa": "LUVA"}
    }

    if 'palavra_atual_portugues' not in st.session_state or st.session_state.get('jogo_portugues_concluido', False):
        palavra_escolhida = random.choice(list(palavras_do_jogo.keys()))
        st.session_state.palavra_atual_portugues = palavra_escolhida
        st.session_state.detalhes_palavra_portugues = palavras_do_jogo[palavra_escolhida]
        st.session_state.jogo_portugues_concluido = False
        st.session_state.mensagem_portugues = ""

    st.markdown(f"### Hmm... qual letra está faltando em: `{st.session_state.palavra_atual_portugues}` ?")

    detalhes = st.session_state.detalhes_palavra_portugues
    opcoes_letras = detalhes["opcoes"] # Renomeei para evitar conflito com a variável 'opcoes' do escopo anterior se houvesse
    letra_correta = detalhes["letra_certa"]
    palavra_completa = detalhes["palavra_completa"]

    cols = st.columns(len(opcoes_letras))
    for i, opcao_letra in enumerate(opcoes_letras):
        if cols[i].button(opcao_letra, key=f"port_{st.session_state.palavra_atual_portugues}_{opcao_letra}"):
            if opcao_letra == letra_correta:
                st.session_state.mensagem_portugues = f"🎉 ISSO AÍ! Você acertou! A palavra é **{palavra_completa}**! 🎉"
                st.session_state.jogo_portugues_concluido = True
                st.balloons()
            else:
                st.session_state.mensagem_portugues = f"😥 Oh, não... A letra '{opcao_letra}' não é a certa. Tente de novo!"
            st.rerun() # Usar st.rerun() é a forma mais moderna e recomendada

    if st.session_state.get('mensagem_portugues'):
        if 'jogo_portugues_concluido' in st.session_state and st.session_state.jogo_portugues_concluido and "acertou" in st.session_state.mensagem_portugues : # Garante que só mostra botão de nova palavra se acertou
            st.success(st.session_state.mensagem_portugues)
            if st.button("Quero outra palavra!", key="port_nova_palavra"):
                st.session_state.jogo_portugues_concluido = True # Força a pegar uma nova palavra na próxima vez
                st.rerun()
        elif 'mensagem_portugues' in st.session_state and st.session_state.mensagem_portugues : # Se tem mensagem mas não concluiu (ou seja, errou)
             st.error(st.session_state.mensagem_portugues)
    st.markdown("---")

elif escolha_da_crianca == "🔢 Matemática Mágica":
    st.title("🔢 Desafios Divertidos com Números!")
    st.image("https://img.freepik.com/vetores-gratis/personagens-de-desenhos-animados-de-conceito-de-educacao-matematica_23-2148500599.jpg?t=st=1716345481~exp=1716349081~hmac=31c3241a7d65f872e078497110fdc7bfae9cf512a8a83f76c6b4e5cb1c5d1675&w=1060", width=300) # Você pode trocar este link de imagem depois!
    st.write("E aí, gênio(a) dos números? Prepare-se para contar, somar, diminuir e resolver mistérios super legais com a matemática!")
    st.info("Em breve: Jogo dos Blocos Lógicos, Desafios de Contagem e Tabuada divertida!", icon="💡")

elif escolha_da_crianca == "🌳 Mundo das Ciências":
    st.title("🌳 Explorando Nosso Mundo Incrível!")
    st.image("https://img.freepik.com/vetores-gratis/ilustracao-do-conceito-de-aula-de-ciencias_114360-19708.jpg?t=st=1716345518~exp=1716349118~hmac=1df1017dbf2549776a42d04a7614d62c32df3957dd790ab086192f0231531f60&w=1060", width=300) # Você pode trocar este link de imagem depois!
    st.write("Olá, cientista mirim! Vamos investigar as plantas, os animais, o nosso corpo e todos os segredos da natureza e do universo!")
    st.info("Em breve: Experiências malucas (e seguras!), curiosidades sobre os dinossauros e muito mais!", icon="💡")

elif escolha_da_crianca == "📜 Viagem pela História do Brasil":
    st.title("📜 Uma Aventura pela História do Nosso Brasil!")
    st.image("https://img.freepik.com/vetores-gratis/mapa-do-brasil-em-estilo-simples-mapa-politico-do-pais-com-as-fronteiras-dos-estados-ilustracao-vetorial_159242-5883.jpg?t=st=1716345576~exp=1716349176~hmac=3e275369ba389a31e6322c50c127565076225626a8ddb1c4972ac991284c5b32&w=740", width=300) # Você pode trocar este link de imagem depois!
    st.write("Prepare sua imaginação para uma viagem no tempo! Vamos conhecer os personagens, os lugares e as histórias que formaram o nosso país tão lindo!")
    st.info("Em breve: Linha do tempo interativa, quem foram os Bandeirantes e a chegada dos portugueses!", icon="💡")

st.markdown("---")
st.markdown("Criado com muito carinho pela Tia Lígia e por você, meu pequeno(a) grande programador(a)! 💖")
