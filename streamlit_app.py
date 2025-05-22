import streamlit as st
import random # Vamos usar para sortear as palavras do nosso jogo!

# --- Configurações da Página e Estilo ---
st.set_page_config(
    page_title="App da Tia Lígia",
    page_icon="📚",  # Um ícone de livro para a aba do navegador
    layout="wide",    # Usa a largura toda da página
    initial_sidebar_state="expanded" # Deixa o menu lateral já aberto
)

# Um pouquinho de CSS para dar um toque especial!
# (CSS é como se fosse a maquiagem e a roupinha da nossa página)
st.markdown("""
<style>
    /* Cor de fundo principal da página */
    .main {
        background-color: #f0f8ff; /* Um azul bem clarinho, "AliceBlue" */
    }
    /* Estilo para os botões (exemplo, pode precisar de ajustes) */
    /* O Streamlit pode ter estilos próprios que se sobrepõem.
        Se este não funcionar como esperado, podemos tentar outras abordagens! */
    .stButton>button {
        background-color: #4CAF50; /* Um verde bonito */
        color: white !important; /* !important para tentar forçar a cor da fonte */
        border-radius: 8px;
        padding: 10px 15px; /* Ajustei um pouco o padding */
        font-weight: bold;
        border: none; /* Remove a borda padrão se houver */
    }
    .stButton>button:hover {
        background-color: #45a049; /* Cor um pouco mais escura ao passar o mouse */
    }
    /* Cor do título principal (h1) da página */
    h1 { /* Afeta st.title() */
        color: #FF6347; /* Um tomate charmoso! */
    }
    /* Cor para subtítulos (h2) */
    h2 { /* Afeta st.header() */
        color: #4682B4; /* Um azul aço bonito */
    }
    /* Cor para sub-subtítulos (h3) */
    h3 { /* Afeta st.subheader() */
        color: #2E8B57; /* Verde mar */
    }
</style>
""", unsafe_allow_html=True)


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
# Ajustando o pronome aqui!
escolha_da_crianca = st.sidebar.selectbox("O que vamos explorar hoje, meu campeão?", lista_de_aventuras)

# --- CONTEÚDO QUE APARECE NA PÁGINA PRINCIPAL ---

if escolha_da_crianca == "🌟 Página Inicial":
    st.title("✨ Bem-vindo de volta ao App da Tia Lígia! ✨") # Será afetado pelo CSS h1
    st.subheader("Eu sou a Tia Lígia, sua Super-Professora, pronta para novas aventuras!") # Será afetado pelo CSS h3
    st.write("Explore o 'Cantinho da Descoberta' aqui do lado 👈 para escolher uma matéria e começar a diversão!")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://img.freepik.com/vetores-gratis/professora-explicando-na-sala-de-aula-com-estudantes_23-2148490575.jpg?t=st=1716345250~exp=1716348850~hmac=a63c7903422502202a13d5375e9a2745dbb0b2f5c49cc8a348b67098ccb3391e&w=1060", caption="Vamos aprender juntos!") # Você pode trocar este link de imagem depois!
    with col2:
        st.markdown("### O que você vai encontrar aqui?") # Este é um h3 no Markdown
        st.markdown("""
        - Jogos e desafios de Português! 🔡
        - Quebra-cabeças de Matemática! 🔢
        - Descobertas incríveis em Ciências! 🌳
        - Aventuras pela História do nosso Brasil! 📜
        - E muito mais no futuro!
        """)
    st.balloons()

# ========== MODIFICAÇÃO COMEÇA AQUI: SEÇÃO DE PORTUGUÊS ==========
elif escolha_da_crianca == "🔡 Português Divertido":
    st.title("🔡 Aventura no Mundo das Palavras!") # h1 (será estilizado pelo CSS)
    st.image("https://img.freepik.com/vetores-gratis/desenhos-animados-de-volta-ao-design-da-escola-com-material-escolar_23-2148588951.jpg?t=st=1716345436~exp=1716349036~hmac=b33a7d544254258679109396a1f848a7d5d29ffdbf6a18b262b019f7bc40505f&w=1060", width=300)
    st.write("Olá, jovem escritor! Vamos brincar com letras e palavras!")
    st.markdown("---")

    # --- Usando ABAS para organizar as atividades de Português ---
    tab_letras_perdidas, tab_mestres_alfabeto, tab_em_breve_port = st.tabs([
        "🧩 Descubra a Letra!",
        "🔍 Mestres do Alfabeto",
        "➕ Mais Aventuras (Em Breve)"
    ])

    # --- ABA 1: Jogo Descubra a Letra Perdida! ---
    with tab_letras_perdidas:
        st.subheader("🎉 Jogo: Descubra a Letra Perdida! 🎉") # h3 (será estilizado)

        palavras_do_jogo = {
            "CA_A": {"letra_certa": "S", "opcoes": ["S", "P", "L"], "palavra_completa": "CASA"},
            "GA_O": {"letra_certa": "T", "opcoes": ["M", "T", "R"], "palavra_completa": "GATO"},
            "BO_A": {"letra_certa": "L", "opcoes": ["N", "P", "L"], "palavra_completa": "BOLA"},
            "MA_Ā": {"letra_certa": "Ç", "opcoes": ["S", "X", "Ç"], "palavra_completa": "MAÇÃ"},
            "LU_A": {"letra_certa": "V", "opcoes": ["B", "F", "V"], "palavra_completa": "LUVA"}
        }

        if 'palavra_atual_portugues' not in st.session_state or st.session_state.get('jogo_portugues_concluido', True): # Se o jogo foi concluído, pega nova palavra
            palavra_escolhida = random.choice(list(palavras_do_jogo.keys()))
            st.session_state.palavra_atual_portugues = palavra_escolhida
            st.session_state.detalhes_palavra_portugues = palavras_do_jogo[palavra_escolhida]
            st.session_state.jogo_portugues_concluido = False
            st.session_state.mensagem_portugues = "" # Limpa mensagem anterior

        st.markdown(f"#### Hmm... qual letra está faltando em: `{st.session_state.palavra_atual_portugues}` ?") # h4

        detalhes = st.session_state.detalhes_palavra_portugues
        opcoes_letras = detalhes["opcoes"]
        letra_correta = detalhes["letra_certa"]
        palavra_completa = detalhes["palavra_completa"]

        cols = st.columns(len(opcoes_letras))
        for i, opcao_letra in enumerate(opcoes_letras):
            if cols[i].button(opcao_letra, key=f"port_letra_{st.session_state.palavra_atual_portugues}_{opcao_letra}"): # Chave um pouco mais robusta
                if opcao_letra == letra_correta:
                    st.session_state.mensagem_portugues = f"🎉 ISSO AÍ! Você acertou! A palavra é **{palavra_completa}**! 🎉"
                    st.session_state.jogo_portugues_concluido = True
                    st.balloons()
                else:
                    st.session_state.mensagem_portugues = f"😥 Oh, não... A letra '{opcao_letra}' não é a certa. Tente de novo!"
                st.rerun()

        if st.session_state.get('mensagem_portugues'):
            if st.session_state.get('jogo_portugues_concluido', False) and "acertou" in st.session_state.mensagem_portugues:
                st.success(st.session_state.mensagem_portugues)
                if st.button("Quero outra palavra!", key="port_nova_palavra"):
                    # A lógica no início do 'if' já vai pegar uma nova palavra por causa de jogo_portugues_concluido = True
                    st.rerun()
            elif st.session_state.get('mensagem_portugues'): # Se tem mensagem (e não é de acerto com jogo concluído)
                 st.error(st.session_state.mensagem_portugues)

    # --- ABA 2: Mestres do Alfabeto e dos Sons ---
    with tab_mestres_alfabeto:
        st.subheader("✨ Alfabeto Mágico ✨") # h3
        st.write("Clique em uma letrinha para ouvir seu nome e ver uma figura bem legal!")

        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num_colunas_alfabeto = 7
        cols_alfabeto = st.columns(num_colunas_alfabeto)

        # Inicializa o estado da letra clicada se não existir
        if 'letra_clicada_alfabeto' not in st.session_state:
            st.session_state.letra_clicada_alfabeto = ""
        if 'info_letra_alfabeto' not in st.session_state:
            st.session_state.info_letra_alfabeto = ""

        for i, letra in enumerate(alfabeto):
            coluna_atual = cols_alfabeto[i % num_colunas_alfabeto]
            if coluna_atual.button(letra, key=f"alf_{letra}", help=f"Descubra mais sobre a letra {letra}!", use_container_width=True):
                st.session_state.letra_clicada_alfabeto = letra
                # Aqui, no futuro, podemos ter um dicionário com informações de cada letra
                # Exemplo: sons_das_letras = {"A": "som de AAAAA", "B": "som de BÊÊÊ"}
                # e imagens: imagens_letras = {"A": "link_imagem_abacate.png", "B": "link_imagem_bola.png"}
                st.session_state.info_letra_alfabeto = f"Você clicou na letra **{letra}**! Que legal! (Em breve: som da letra 🔊, palavra exemplo 🍎 e figura!)"
                st.rerun() # Para mostrar a info atualizada

        if st.session_state.letra_clicada_alfabeto and st.session_state.info_letra_alfabeto:
            st.success(st.session_state.info_letra_alfabeto, icon="🌟")

        st.markdown("---")
        st.subheader("🔡 Vogais e Consoantes 🔡") # h3
        st.write("Você sabe a diferença? Vamos aprender brincando!")
        st.image("https://img.freepik.com/vetores-premium/alfabeto-bonito-dos-desenhos-animados-com-vogais-destacadas-em-vermelho_811768-1404.jpg?w=900", width=400, caption="As vogais são A, E, I, O, U. Todas as outras letrinhas do alfabeto são as consoantes!")
        st.info("Em breve: um jogo super divertido para encontrar as vogais e as consoantes!", icon="🎮")


    # --- ABA 3: Em Breve ---
    with tab_em_breve_port:
        st.info("Aguarde! Mais aventuras com as palavras estão chegando em breve nesta aba!", icon="🚀")
        st.image("https://img.freepik.com/vetores-gratis/criancas-felizes-brincando-juntas_23-2149213103.jpg?t=st=1716358032~exp=1716361632~hmac=e5846a413d66c9637ca8e58b4e5d37161e2f73a6162f0ba7b7df726042f7542d&w=1060", width=400)
# ========== MODIFICAÇÃO TERMINA AQUI: SEÇÃO DE PORTUGUÊS ==========

elif escolha_da_crianca == "🔢 Matemática Mágica":
    st.title("🔢 Desafios Divertidos com Números!") # h1
    st.image("https://img.freepik.com/vetores-gratis/personagens-de-desenhos-animados-de-conceito-de-educacao-matematica_23-2148500599.jpg?t=st=1716345481~exp=1716349081~hmac=31c3241a7d65f872e078497110fdc7bfae9cf512a8a83f76c6b4e5cb1c5d1675&w=1060", width=300)
    st.write("E aí, gênio dos números? Prepare-se para contar, somar, diminuir e resolver mistérios super legais com a matemática!")
    st.info("Em breve: Jogo dos Blocos Lógicos, Desafios de Contagem e Tabuada divertida!", icon="💡")

elif escolha_da_crianca == "🌳 Mundo das Ciências":
    st.title("🌳 Explorando Nosso Mundo Incrível!") # h1
    st.image("https://img.freepik.com/vetores-gratis/ilustracao-do-conceito-de-aula-de-ciencias_114360-19708.jpg?t=st=1716345518~exp=1716349118~hmac=1df1017dbf2549776a42d04a7614d62c32df3957dd790ab086192f0231531f60&w=1060", width=300)
    st.write("Olá, cientista mirim! Vamos investigar as plantas, os animais, o nosso corpo e todos os segredos da natureza e do universo!")
    st.info("Em breve: Experiências malucas (e seguras!), curiosidades sobre os dinossauros e muito mais!", icon="💡")

elif escolha_da_crianca == "📜 Viagem pela História do Brasil":
    st.title("📜 Uma Aventura pela História do Nosso Brasil!") # h1
    st.image("https://img.freepik.com/vetores-gratis/mapa-do-brasil-em-estilo-simples-mapa-politico-do-pais-com-as-fronteiras-dos-estados-ilustracao-vetorial_159242-5883.jpg?t=st=1716345576~exp=1716349176~hmac=3e275369ba389a31e6322c50c127565076225626a8ddb1c4972ac991284c5b32&w=740", width=300)
    st.write("Prepare sua imaginação para uma viagem no tempo! Vamos conhecer os personagens, os lugares e as histórias que formaram o nosso país tão lindo!")
    st.info("Em breve: Linha do tempo interativa, quem foram os Bandeirantes e a chegada dos portugueses!", icon="💡")

st.markdown("---")
# Ajustando a mensagem final para celebrar nosso programador!
st.markdown("Criado com muito carinho pela Tia Lígia e por você, nosso grande programador! 💖")
