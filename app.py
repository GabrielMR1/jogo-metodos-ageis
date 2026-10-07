import streamlit as st

# 1. Configuração inicial da página web
st.set_page_config(
    page_title="Curiosidades Ágeis - Dashboard Game",
    page_icon="🎴",
    layout="centered"
)

# 2. Banco de Dados das Cartas de Curiosidade
# Lista de Cartas: Métodos Ágeis (Perguntas Fáceis e Diretas)
CARTAS = [
    {
        "categoria": "Manifesto Ágil",
        "curiosidade": "O Manifesto Ágil foi criado em 2001 e valoriza entregas rápidas de software funcionando mais do que documentações gigantescas.",
        "pergunta": "O que o Manifesto Ágil prioriza acima de processos e ferramentas?",
        "opcoes": [
            "Indivíduos e interações entre as pessoas",
            "Contratos longos e rígidos",
            "Relatórios semanais em PDF",
            "Manuais impressos"
        ],
        "resposta_correta": 0,
        "explicacao": "O primeiro valor do Manifesto Ágil é: 'Indivíduos e interações mais que processos e ferramentas'."
    },
    {
        "categoria": "Scrum / Eventos",
        "curiosidade": "A Daily Scrum é uma reunião diária bem rápida para a equipe alinhar o que fez ontem, o que fará hoje e se há algum impedimento.",
        "pergunta": "Qual é a duração máxima recomendada para a reunião diária (Daily Scrum)?",
        "opcoes": ["1 hora", "30 minutos", "15 minutos", "5 minutos"],
        "resposta_correta": 2,
        "explicacao": "A Daily deve ser objetiva e dura no máximo 15 minutos para não tomar o tempo de desenvolvimento da equipe."
    },
    {
        "categoria": "Scrum / Ciclos",
        "curiosidade": "No Scrum, o trabalho é dividido em pequenos blocos de tempo fixos (geralmente de 1 a 4 semanas) onde a equipe entrega funcionalidades prontas.",
        "pergunta": "Como é chamado esse ciclo de tempo fixo de trabalho no Scrum?",
        "opcoes": ["Sprint", "Maratona", "Turno", "Etapa Fictícia"],
        "resposta_correta": 0,
        "explicacao": "No Scrum, chamamos de 'Sprint' cada ciclo de trabalho focado na entrega de um incremento do produto."
    },
    {
        "categoria": "Scrum / Papéis",
        "curiosidade": "No Scrum existem três papéis principais: Product Owner, Scrum Master e Desenvolvedores.",
        "pergunta": "Qual é o papel responsável por priorizar a lista de tarefas (Backlog) e representar os interesses do cliente?",
        "opcoes": [
            "Product Owner (PO)",
            "Scrum Master",
            "Programador Estagiário",
            "Gerente de Suporte"
        ],
        "resposta_correta": 0,
        "explicacao": "O Product Owner (PO) define as prioridades do que deve ser feito com base no valor para o negócio."
    },
    {
        "categoria": "Kanban / Gestão Visual",
        "curiosidade": "O Kanban usa cartões coloridos em um quadro dividido em colunas simples como: 'A Fazer', 'Em Andamento' e 'Concluído'.",
        "pergunta": "Qual é o objetivo principal de utilizar o quadro Kanban no projeto?",
        "opcoes": [
            "Visualizar facilmente o fluxo e o status do trabalho",
            "Aumentar a quantidade de reuniões presenciais",
            "Esconder as tarefas que estão atrasadas",
            "Substituir o código-fonte do sistema"
        ],
        "resposta_correta": 0,
        "explicacao": "O Kanban serve como um painel visual simples para dar transparência ao progresso do trabalho."
    },
    {
        "categoria": "Extreme Programming (XP)",
        "curiosidade": "O XP (Extreme Programming) foca na qualidade do código e na colaboração próxima dos programadores.",
        "pergunta": "Na prática de 'Programação em Par' (Pair Programming), quantos desenvolvedores trabalham juntos no mesmo computador?",
        "opcoes": ["2 desenvolvedores", "5 desenvolvedores", "A equipe inteira de 20 pessoas", "Apenas 1 desenvolvedor"],
        "resposta_correta": 0,
        "explicacao": "Na Programação em Par, 2 desenvolvedores trabalham juntos: um digita o código (Piloto) e o outro analisa e revisa (Navegador)."
    }
]

# 3. Gerenciamento de Estado do Jogo (Session State)
if "indice" not in st.session_state:
    st.session_state.indice = 0
if "pontos" not in st.session_state:
    st.session_state.pontos = 0
if "respondido" not in st.session_state:
    st.session_state.respondido = False
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# 4. Cabeçalho do Dashboard
st.title("🎴 Curiosidades Ágeis - Dashboard Game")
st.caption("Engenharia de Software — Jogo Interativo de Revisão de Métodos Ágeis")

# 5. Painel de Indicadores / Métrica (Dashboard)
col1, col2, col3 = st.columns(3)
col1.metric("Pontuação", f"{st.session_state.pontos} pts")
col2.metric("Carta Atual", f"{min(st.session_state.indice + 1, len(CARTAS))} / {len(CARTAS)}")
progresso = st.session_state.indice / len(CARTAS)
col3.metric("Progresso", f"{int(min(progresso, 1.0) * 100)}%")
st.progress(min(progresso, 1.0))

st.markdown("---")

# 6. Lógica de Navegação e Fim do Jogo
if st.session_state.indice >= len(CARTAS):
    st.balloons()
    st.success("🎉 **Parabéns! Você concluiu o Desafio de Métodos Ágeis!**")
    st.subheader(f"Pontuação Final: **{st.session_state.pontos} de {len(CARTAS) * 10} pontos**.")
    
    if st.button("🔄 Reiniciar Jogo"):
        st.session_state.indice = 0
        st.session_state.pontos = 0
        st.session_state.respondido = False
        st.session_state.feedback = ""
        st.rerun()
else:
    carta = CARTAS[st.session_state.indice]
    
    # Exibição da Carta
    st.subheader(f"📌 Categoria: {carta['categoria']}")
    st.info(f"💡 **Curiosidade:** {carta['curiosidade']}")
    st.write(f"### ❓ {carta['pergunta']}")
    
    escolha = st.radio(
        "Escolha a alternativa correta:",
        carta["opcoes"],
        key=f"q_{st.session_state.indice}"
    )
    
    # Confirmação da resposta
    if not st.session_state.respondido:
        if st.button("Confirmar Resposta"):
            st.session_state.respondido = True
            idx_escolha = carta["opcoes"].index(escolha)
            if idx_escolha == carta["resposta_correta"]:
                st.session_state.pontos += 10
                st.session_state.feedback = "correto"
            else:
                st.session_state.feedback = "incorreto"
            st.rerun()
    else:
        if st.session_state.feedback == "correto":
            st.success(f"✅ **Resposta Correta! (+10 pontos)**\n\n_{carta['explicacao']}_")
        else:
            st.error(f"❌ **Resposta Incorreta!**\n\n_{carta['explicacao']}_")
            
        if st.button("Próxima Carta ➔"):
            st.session_state.indice += 1
            st.session_state.respondido = False
            st.session_state.feedback = ""
            st.rerun()