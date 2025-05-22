import streamlit as st
import random # Vamos usar para sortear as palavras, os números e os animais!

# --- Configurações da Página e Estilo ---
st.set_page_config(
    page_title="App da Tia Lígia",
    page_icon="📚",  # Um ícone de livro para a aba do navegador
    layout="wide",    # Usa a largura toda da página
    initial_sidebar_state="expanded" # Deixa o menu lateral já aberto
)

# Um pouquinho de CSS para dar um toque especial!
st.markdown("""
<style>
    /* Cor de fundo principal da página */
    .main {
        background-color: #f0f8ff; /* Um azul bem clarinho, "AliceBlue" */
    }
    /* Estilo para os botões */
    .stButton>button {
        background-color: #4CAF50; /* Um verde bonito */
        color: white !important;
        border-radius: 8px;
        padding: 10px 15px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    h1 { color: #FF6347; } /* Laranja avermelhado para títulos principais */
    h2 { color: #4682B4; } /* Azul aço para headers */
    h3 { color: #2E8B57; } /* Verde mar para subheaders */
</style>
""", unsafe_allow_html=True)


# --- NOSSO MENU SECRETO NA LATERAL (SIDEBAR) ---
st.sidebar.title("🎒 Cantinho da Descoberta 🎒")
st.sidebar.markdown("---")
st.sidebar.image("https://img.freepik.com/vetores-gratis/menina-bonita-crianca-feliz-dos-desenhos-animados-com-livro_701961-2227.jpg?t=st=1716345038~exp=1716348638~hmac=2e3924f57d1252306177a3c68e72222cd8f160a0e2437e0e84808894ab8db76e&w=740", width=150)
st.sidebar.markdown("---")

lista_de_aventuras = [
    "🌟 Página Inicial",
    "🔡 Português Divertido",
    "🔢 Matemática Mágica",
    "🌳 Mundo das Ciências",
    "🌍 Geografia Divertida", 
    "📜 Viagem pela História do Brasil"
]
escolha_da_crianca = st.sidebar.selectbox("Qual aventura vamos descobrir?", lista_de_aventuras)

# --- CONTEÚDO QUE APARECE NA PÁGINA PRINCIPAL ---

if escolha_da_crianca == "🌟 Página Inicial":
    st.title("✨ Bem-vindo de volta ao App da Tia Lígia! ✨")
    st.subheader("Eu sou a Tia Lígia, sua Super-Professora, pronta para novas aventuras!")
    st.write("Explore o 'Cantinho da Descoberta' aqui do lado 👈 para escolher uma matéria e começar a diversão!")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://img.freepik.com/vetores-gratis/professora-explicando-na-sala-de-aula-com-estudantes_23-2148490575.jpg?t=st=1716345250~exp=1716348850~hmac=a63c7903422502202a13d5375e9a2745dbb0b2f5c49cc8a348b67098ccb3391e&w=1060", caption="Vamos aprender juntos!")
    with col2:
        st.markdown("### O que você vai encontrar aqui?")
        st.markdown("""
        - Jogos e desafios de Português! 🔡
        - Quebra-cabeças de Matemática! 🔢
        - Descobertas incríveis em Ciências! 🌳
        - Aventuras pela Geografia! 🌍
        - Viagens pela História do nosso Brasil! 📜
        - E muito mais no futuro!
        """)
    st.balloons()

elif escolha_da_crianca == "🔡 Português Divertido":
    st.title("🔡 Aventura no Mundo das Palavras!")
    st.image("https://img.freepik.com/vetores-gratis/desenhos-animados-de-volta-ao-design-da-escola-com-material-escolar_23-2148588951.jpg?t=st=1716345436~exp=1716349036~hmac=b33a7d544254258679109396a1f848a7d5d29ffdbf6a18b262b019f7bc40505f&w=1060", width=300)
    st.write("Olá, jovem escritor! Vamos brincar com letras e palavras!")
    st.markdown("---")

    tab_letras_perdidas, tab_mestres_alfabeto, tab_em_breve_port = st.tabs([
        "🧩 Descubra a Letra!",
        "🔍 Mestres do Alfabeto",
        "➕ Mais Aventuras (Em Breve)"
    ])

    with tab_letras_perdidas:
        st.subheader("🎉 Jogo: Descubra a Letra Perdida! 🎉")
        palavras_do_jogo = {
            "CA_A": {"letra_certa": "S", "opcoes": ["S", "P", "L"], "palavra_completa": "CASA"},
            "GA_O": {"letra_certa": "T", "opcoes": ["M", "T", "R"], "palavra_completa": "GATO"},
            "BO_A": {"letra_certa": "L", "opcoes": ["N", "P", "L"], "palavra_completa": "BOLA"},
            "MA_Ā": {"letra_certa": "Ç", "opcoes": ["S", "X", "Ç"], "palavra_completa": "MAÇÃ"},
            "LU_A": {"letra_certa": "V", "opcoes": ["B", "F", "V"], "palavra_completa": "LUVA"}
        }

        if 'palavra_atual_portugues' not in st.session_state or st.session_state.get('jogo_portugues_concluido', True):
            palavra_escolhida = random.choice(list(palavras_do_jogo.keys()))
            st.session_state.palavra_atual_portugues = palavra_escolhida
            st.session_state.detalhes_palavra_portugues = palavras_do_jogo[palavra_escolhida]
            st.session_state.jogo_portugues_concluido = False
            st.session_state.mensagem_portugues = ""

        st.markdown(f"#### Hmm... qual letra está faltando em: `{st.session_state.palavra_atual_portugues}` ?")

        detalhes = st.session_state.detalhes_palavra_portugues
        opcoes_letras = detalhes["opcoes"]
        letra_correta = detalhes["letra_certa"]
        palavra_completa = detalhes["palavra_completa"]

        cols = st.columns(len(opcoes_letras))
        for i, opcao_letra in enumerate(opcoes_letras):
            if cols[i].button(opcao_letra, key=f"port_letra_{st.session_state.palavra_atual_portugues}_{opcao_letra}"):
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
                    st.rerun()
            elif st.session_state.get('mensagem_portugues'):
                 st.error(st.session_state.mensagem_portugues)

    with tab_mestres_alfabeto:
        st.subheader("✨ Alfabeto Mágico com Som! ✨")
        st.write("Clique em uma letrinha para ouvir seu nome!")

        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num_colunas_alfabeto = 7
        cols_alfabeto = st.columns(num_colunas_alfabeto)

        if 'letra_clicada_nesta_aba' not in st.session_state:
             st.session_state.letra_clicada_nesta_aba = None

        for i, letra in enumerate(alfabeto):
            coluna_atual = cols_alfabeto[i % num_colunas_alfabeto]
            if coluna_atual.button(letra, key=f"alf_{letra}", help=f"Descubra mais sobre a letra {letra}!", use_container_width=True):
                st.session_state.letra_clicada_alfabeto = letra
                st.session_state.letra_clicada_nesta_aba = letra
        
        if st.session_state.letra_clicada_nesta_aba:
            letra_para_mostrar = st.session_state.letra_clicada_nesta_aba
            st.success(f"Você clicou na letra **{letra_para_mostrar}**!", icon="🌟")
            
            github_user = "Yaakov-Israel"
            github_repo = "app-tia-ligia"
            branch_name = "main"
            
            url_base_audio = f"https://raw.githubusercontent.com/{github_user}/{github_repo}/{branch_name}/sons_alfabeto/" 
            caminho_audio_url = f"{url_base_audio}{letra_para_mostrar}.mp3" 
            
            st.write(f"Tentando tocar o som pela URL: {caminho_audio_url}") 
            
            try:
                st.audio(caminho_audio_url, format="audio/mp3")
                st.caption(f"Tocando som para a letra {letra_para_mostrar}! Se não ouvir, confira a URL acima (ela deve abrir o som no navegador se você colar lá), verifique se o arquivo {letra_para_mostrar}.mp3 existe MESMO na pasta 'sons_alfabeto' do seu GitHub e se o volume do seu computador está ligado. 😉")
            except Exception as e:
                st.error(f"Oops! Tive um problema ao tentar carregar o som da letra {letra_para_mostrar} pela URL.")
                st.error(f"URL que tentei usar: {caminho_audio_url}")
                st.error(f"Detalhe técnico do erro: {e}")
                st.warning("Verifique se a pasta 'sons_alfabeto' e o arquivo .mp3 existem no GitHub com os nomes idênticos (maiúsculas e minúsculas são super importantes!). O repositório precisa ser público para o Streamlit acessar os arquivos de áudio assim.")

            st.markdown("(Em breve: exemplos e figuras!)")
            st.session_state.letra_clicada_nesta_aba = None 


        st.markdown("---")
        st.subheader("🔡 Vogais e Consoantes 🔡")
        st.write("Você sabe a diferença? Vamos aprender brincando!")
        st.image("https://img.freepik.com/vetores-premium/alfabeto-bonito-dos-desenhos-animados-com-vogais-destacadas-em-vermelho_811768-1404.jpg?w=900", width=400, caption="As vogais são A, E, I, O, U. Todas as outras letrinhas do alfabeto são as consoantes!")
        st.info("Em breve: um jogo super divertido para encontrar as vogais e as consoantes!", icon="🎮")

    with tab_em_breve_port:
        st.info("Aguarde! Mais aventuras com as palavras estão chegando em breve nesta aba!", icon="🚀")
        st.image("https://img.freepik.com/vetores-gratis/criancas-felizes-brincando-juntas_23-2149213103.jpg?t=st=1716358032~exp=1716361632~hmac=e5846a413d66c9637ca8e58b4e5d37161e2f73a6162f0ba7b7df726042f7542d&w=1060", width=400)

elif escolha_da_crianca == "🔢 Matemática Mágica":
    st.title("🔢 Desafios Divertidos com Números!")
    st.image("https://img.freepik.com/vetores-gratis/personagens-de-desenhos-animados-de-conceito-de-educacao-matematica_23-2148500599.jpg?t=st=1716345481~exp=1716349081~hmac=31c3241a7d65f872e078497110fdc7bfae9cf512a8a83f76c6b4e5cb1c5d1675&w=1060", width=300)
    st.write("E aí, gênio dos números? Prepare-se para contar, somar, diminuir e resolver mistérios super legais com a matemática!")
    st.markdown("---")

    st.subheader("➕ Quanto é? Desafio da Soma! ➕")

    if 'num1_soma' not in st.session_state or st.session_state.get('mat_jogo_concluido', True):
        st.session_state.num1_soma = random.randint(1, 10)
        st.session_state.num2_soma = random.randint(1, 10)
        st.session_state.resposta_correta_soma = st.session_state.num1_soma + st.session_state.num2_soma
        st.session_state.mat_jogo_concluido = False
        st.session_state.mat_mensagem = ""
        if 'resposta_usuario_soma' in st.session_state:
            del st.session_state['resposta_usuario_soma']

    st.markdown(f"### Resolva esta continha:  `{st.session_state.num1_soma} + {st.session_state.num2_soma} = ?`")
    resposta_usuario = st.number_input("Qual a sua resposta, gênio?", min_value=0, step=1, key=f"resposta_soma_{st.session_state.num1_soma}_{st.session_state.num2_soma}", value=None)

    if st.button("Conferir Resposta!", key="btn_conferir_soma"):
        if resposta_usuario is not None:
            if int(resposta_usuario) == st.session_state.resposta_correta_soma:
                st.session_state.mat_mensagem = f"🎉 PARABÉNS! Você acertou em cheio! {st.session_state.num1_soma} + {st.session_state.num2_soma} = {st.session_state.resposta_correta_soma}! 🎉"
                st.session_state.mat_jogo_concluido = True
                st.balloons()
            else:
                st.session_state.mat_mensagem = f"😥 Quase lá! A resposta não é {int(resposta_usuario)}. Tente pensar um pouquinho mais! Dica: conte nos dedinhos se precisar! 😉"
                st.session_state.mat_jogo_concluido = False
        else:
            st.session_state.mat_mensagem = "Digite sua resposta primeiro, meu campeão!"
            st.session_state.mat_jogo_concluido = False

    if st.session_state.get('mat_mensagem'):
        if st.session_state.get('mat_jogo_concluido', False) and "PARABÉNS" in st.session_state.mat_mensagem :
            st.success(st.session_state.mat_mensagem)
            if st.button("Quero um Novo Desafio!", key="mat_novo_desafio"):
                st.rerun()
        elif st.session_state.get('mat_mensagem'):
            if "Digite sua resposta" in st.session_state.mat_mensagem:
                st.warning(st.session_state.mat_mensagem)
            else:
                st.error(st.session_state.mat_mensagem)

    st.markdown("---")
    st.info("Em breve: Jogo dos Blocos Lógicos, Desafios de Contagem e Tabuada divertida!", icon="💡")

elif escolha_da_crianca == "🌳 Mundo das Ciências":
    st.title("🌳 Explorando Nosso Mundo Incrível!")
    st.image("https://img.freepik.com/vetores-gratis/ilustracao-do-conceito-de-aula-de-ciencias_114360-19708.jpg?t=st=1716345518~exp=1716349118~hmac=1df1017dbf2549776a42d04a7614d62c32df3957dd790ab086192f0231531f60&w=1060", width=300)
    st.write("Olá, cientista mirim! Vamos investigar as plantas, os animais, o nosso corpo e todos os segredos da natureza e do universo!")
    st.markdown("---")

    st.subheader("🐾 Bichos Curiosos e Seus Segredos! 🐾")

    github_user_para_imagens = "Yaakov-Israel" 
    github_repo_para_imagens = "app-tia-ligia" 
    branch_name_para_imagens = "main"         
    nome_da_pasta_de_imagens = "imagens_animais" 

    url_base_imagens_animais = f"https://raw.githubusercontent.com/{github_user_para_imagens}/{github_repo_para_imagens}/{branch_name_para_imagens}/{nome_da_pasta_de_imagens}/"

    animais_data = [
        {
            "nome": "Cachorro",
            "imagem_url": f"{url_base_imagens_animais}Cachorro.webp", 
            "fato": "O cachorro é o melhor amigo do ser humano e existem muitas raças diferentes, como esse filhote fofo que você encontrou!"
        },
        {
            "nome": "Gato",
            "imagem_url": f"{url_base_imagens_animais}Gato.jpg", 
            "fato": "Os gatos são conhecidos por seus miados charmosos e por adorarem caixas de papelão!"
        },
        {
            "nome": "Esquilo",
            "imagem_url": f"{url_base_imagens_animais}Esquilo.jpg", 
            "fato": "Os esquilos são roedores espertos que adoram guardar nozes para o inverno!"
        },
        {
            "nome": "Axolote",
            "imagem_url": f"{url_base_imagens_animais}axolote.jpg", 
            "fato": "O axolote é uma salamandra mexicana muito especial que consegue regenerar partes do corpo, como se fosse um super-herói!"
        },
        {
            "nome": "Ornitorrinco",
            "imagem_url": f"{url_base_imagens_animais}ornitorrinco.png", 
            "fato": "O ornitorrinco é um animalzinho único da Austrália: tem bico de pato, pelo de mamífero e ainda bota ovos!"
        },
        {
            "nome": "Bicho-preguiça",
            "imagem_url": f"{url_base_imagens_animais}bicho-preguica.webp", 
            "fato": "A preguiça se move bem devagarinho pelas árvores e adora tirar um cochilo!"
        },
         {
            "nome": "Pinguim",
            "imagem_url": f"{url_base_imagens_animais}pinguim.jpg", 
            "fato": "Os pinguins são aves que não voam, mas são excelentes nadadores! Eles vivem em lugares bem frios."
        }
    ]
    
    if 'animal_atual_idx' not in st.session_state: 
        st.session_state.animal_atual_idx = random.choice(range(len(animais_data)))
        
    if st.button("Próximo Animal Curioso!", key="btn_prox_animal_curioso"):
        indice_anterior = st.session_state.animal_atual_idx
        if len(animais_data) > 1:
            novo_indice = random.choice([i for i in range(len(animais_data)) if i != indice_anterior])
        else: 
            novo_indice = indice_anterior
        st.session_state.animal_atual_idx = novo_indice
        st.rerun() 

    animal_idx = st.session_state.get('animal_atual_idx', 0) 
    animal_atual = animais_data[animal_idx]

    st.markdown(f"### Conheça o(a): **{animal_atual['nome']}**")
    
    st.write(f"Tentando mostrar imagem de: {animal_atual['imagem_url']}")
    try:
        st.image(animal_atual['imagem_url'], caption=f"Um(a) lindo(a) {animal_atual['nome']}!", width=400)
    except Exception as e:
        st.error(f"Oops! Não consegui carregar a foto do(a) {animal_atual['nome']}. Verifique se o arquivo '{animal_atual['imagem_url'].split('/')[-1]}' está na pasta '{nome_da_pasta_de_imagens}' no GitHub e se a URL está correta. (Erro: {e})")

    st.info(f"**Curiosidade:** {animal_atual['fato']}", icon="💡")

    st.markdown("---")
    st.success("Em breve: Quizzes sobre animais, seus sons e onde eles vivem!", icon="🧐")

elif escolha_da_crianca == "🌍 Geografia Divertida":
    st.title("🌍 Explorando o Planeta Terra!")
    st.image("https://img.freepik.com/vetores-gratis/ilustracao-do-conceito-de-planeta-terra_114360-10015.jpg?w=1060", width=300) 
    st.write("Olá, pequeno explorador! Vamos descobrir os segredos do nosso planeta, os países, os mapas e muito mais!")
    st.markdown("---")

    st.subheader("🗺️ Viagem pelos Continentes! 🗺️")
    
    continentes_data = [
        {
            "nome": "América do Sul",
            "imagem_url": "https://img.freepik.com/vetores-gratis/mapa-da-america-do-sul-com-paises_23-2148002062.jpg?w=740", 
            "fato": "É onde fica o nosso amado Brasil e a gigantesca Floresta Amazônica, o pulmão do mundo!",
            "icone": "🇧🇷"
        },
        {
            "nome": "Europa",
            "imagem_url": "https://img.freepik.com/vetores-gratis/mapa-da-europa_23-2147514985.jpg?w=740", 
            "fato": "Um continente cheio de castelos antigos, reis, rainhas e onde nasceram muitas das histórias que conhecemos!",
            "icone": "🏰"
        },
        {
            "nome": "África",
            "imagem_url": "https://img.freepik.com/vetores-gratis/mapa-da-africa_23-2147514978.jpg?w=740", 
            "fato": "É o berço da humanidade! Tem desertos enormes, savanas com animais incríveis como leões e elefantes.",
            "icone": "🦁"
        },
        {
            "nome": "Ásia",
            "imagem_url": "https://img.freepik.com/vetores-gratis/mapa-da-asia_23-2147514980.jpg?w=740", 
            "fato": "O maior de todos os continentes! É lá que fica a Muralha da China e o Monte Everest, o ponto mais alto da Terra!",
            "icone": "🐼" 
        },
        {
            "nome": "América do Norte",
            "imagem_url": "https://img.freepik.com/vetores-gratis/mapa-da-america-do-norte_23-2147514979.jpg?w=740", 
            "fato": "Tem países enormes como o Canadá (terra do xarope de bordo!) e os Estados Unidos (terra da Estátua da Liberdade!).",
            "icone": "🍁" 
        },
        {
            "nome": "Oceania",
            "imagem_url": "https://img.freepik.com/vetores-gratis/mapa-da-australia_23-2147514981.jpg?w=740", 
            "fato": "Um continente formado por muitas ilhas e onde fica a Austrália, terra dos cangurus e coalas!",
            "icone": "🐨"
        },
        {
            "nome": "Antártida",
            "imagem_url": "https://img.freepik.com/vetores-gratis/mapa-da-antartida_23-2147514986.jpg?w=740", 
            "fato": "O lugar mais frio do nosso planeta! É coberto de gelo e lá vivem os pinguins imperadores.",
            "icone": "🐧"
        }
    ]

    if 'continente_atual_idx' not in st.session_state:
        st.session_state.continente_atual_idx = random.choice(range(len(continentes_data)))

    if st.button("Próximo Continente!", key="btn_prox_continente"):
        indice_anterior = st.session_state.continente_atual_idx
        if len(continentes_data) > 1:
            novo_indice = random.choice([i for i in range(len(continentes_data)) if i != indice_anterior])
        else:
            novo_indice = indice_anterior
        st.session_state.continente_atual_idx = novo_indice
        st.rerun()

    continente_idx = st.session_state.get('continente_atual_idx', 0)
    continente_atual = continentes_data[continente_idx]

    st.markdown(f"### {continente_atual['icone']} Bem-vindo à {continente_atual['nome']}! {continente_atual['icone']}")
    
    st.write(f"Tentando mostrar imagem de: {continente_atual['imagem_url']}")
    try:
        st.image(continente_atual['imagem_url'], caption=f"Mapa ou imagem da {continente_atual['nome']}", width=450)
    except Exception as e:
        st.error(f"Oops! Não consegui carregar a imagem da {continente_atual['nome']}. (Erro: {e})")
        st.warning(f"A URL da imagem que tentei usar foi: {continente_atual['imagem_url']}")

    st.info(f"**Você Sabia?** {continente_atual['fato']}", icon="💡")
    
    st.markdown("---")
    st.success("Em breve: Caça ao tesouro com mapas, curiosidades sobre países e muito mais!", icon="🗺️")

# ========== MODIFICAÇÃO COMEÇA AQUI: SEÇÃO DE HISTÓRIA DO BRASIL ==========
elif escolha_da_crianca == "📜 Viagem pela História do Brasil":
    st.title("📜 Uma Aventura pela História do Nosso Brasil!")
    # Você pode trocar esta imagem por uma mais específica sobre os povos originários ou a chegada dos portugueses!
    st.image("https://img.freepik.com/vetores-gratis/mapa-do-brasil-em-estilo-simples-mapa-politico-do-pais-com-as-fronteiras-dos-estados-ilustracao-vetorial_159242-5883.jpg?w=740", width=300) 
    st.write("Prepare sua imaginação para uma viagem no tempo! Vamos conhecer os personagens, os lugares e as histórias que formaram o nosso país tão lindo!")
    st.markdown("---")

    st.subheader("🏹 Quem Já Morava Aqui? Os Povos Originários! 🏹")
    
    # Para esta imagem, você pode procurar no Freepik por "crianças indígenas Brasil desenho" ou "aldeia indígena ilustração"
    # e substituir a URL abaixo. Ou subir sua própria imagem para a pasta 'imagens_historia' no GitHub.
    # Exemplo de URL se você subir: f"https://raw.githubusercontent.com/Yaakov-Israel/app-tia-ligia/main/imagens_historia/povos_originarios.jpg"
    st.image("https://img.freepik.com/vetores-gratis/grupo-de-criancas-indigenas-em-trajes-tradicionais_23-2148998592.jpg?w=1060", 
             caption="Os primeiros corações a baterem em nossa terra.", width=450)

    st.write("""
    Muito, muito tempo atrás, antes mesmo de o Brasil se chamar Brasil, estas terras já tinham donos! 
    Eram os **Povos Originários**, também conhecidos como indígenas. 🌳🦜

    Eles não eram um povo só, mas MUITOS povos diferentes! Cada um com sua língua, seus costumes, 
    suas músicas, suas danças e suas histórias incríveis passadas de geração em geração. 
    Alguns exemplos de povos são os Tupis, os Guaranis, os Ianomâmis, os Xavantes, e tantos outros!

    Eles viviam em harmonia com a natureza, conheciam todos os segredos da floresta, dos rios e dos animais. 
    Sabiam quais plantas curavam, quais alimentos a terra dava, e como viver cuidando do nosso planeta. 💚
    Suas casas, as ocas, eram feitas com materiais da natureza, e suas aldeias eram cheias de vida comunitária.
    """)
    
    st.info("""
    **Você Sabia?** Muitas palavras que usamos hoje em português vieram das línguas indígenas, como: 
    *capim, mingau, pipoca, abacaxi, jacaré, tatu* e muitas outras! Que legal, né? 😊
    """, icon="💡")

    st.markdown("---")
    st.success("Em breve: A chegada dos portugueses, as grandes navegações e muito mais da nossa história!", icon="⏳")

# ========== MODIFICAÇÃO TERMINA AQUI: SEÇÃO DE HISTÓRIA DO BRASIL ==========

st.markdown("---")
st.markdown("Criado com muito carinho pela Tia Lígia para você! ❤️")
