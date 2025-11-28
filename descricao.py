

class Descricao:
    descricao = "airbnb p/ cachorros"
    tabelas = ["tutor", "pet"]  # falou algo sobre o tutor ter uma credencial
    aplicacao = "React JS"
    ferramenta_de_criacao = "Vite"
    nao_ficou_claro_o_nome = ["componente", "estado", "transição de estado"]
    lovable = "Sugerido durante o reconhecimento ou produção"
    nao_ficou_claro_o_nome = ["páginas = rotas (pro frontend)", "React Router DOM"]
    estilos = ["css", "styled component (nunca ouvi falar)", "tailwind css"]
    interacao_com_API_REST = [
        "mock com JSON server (não sei o que é)", 
    ]
    # Fazer chamadas, receber dados
    interacao_meu_React_com_API = [
        "fetch API do JS", 
        "axios",
        "React Query (hooks)"
    ]

    # Ele não trás coisas estruturadas (ele é meio maluco)
    # Como consequência, há coisas que não ficam claras e preciso de ajuda com elas
    coisas_soltas_faladas = [
        "Context API - algo sobre Hooks - algo sobre guardar usuário num contexto global",
        "Rotas autenticadas (não faço ideia do que seja)"
    ]
    
    # Descrição do que ele quer ver
    visao = [
        "Cadastro de tutores",
        "Listagem de cartões (clique) = exibe animais",
        "Na listagem dos animais: formulário de add novo animal",
        "Na criação dos animais (sugerido UPLOAD de foto do animal)"
    ]

    visao_continuacao = [
        "Abrir na página de cadastro (Deve ser o cadastro de tutor)",
        "Nome - email - senha = cadastro",
        "Login - entrou",
        "Caiu na tela principal",
        "Ideia minha --> mostrar todos os tutores e o acesso aos seus animais"
    ]

    deploy = [
        "Vercel (nunca coloquei um projeto na Vercel, que use backend)"
    ]

    pesquisar = [
        "Como gerenciar estados de formulários (devido ter vários campos)",
        "Como fazer autenticação (é com React ou junto ao React)?",
        "Como fazer deploy de um projeto com backend, na Vercel?"
    ]

class Instalacao:
    comando = "npm create vite@latest nome-do-meu-projeto -- --template react"
    comando_ts = "npm create vite@latest . -- --template react-ts"

class IniciarServidor:
    comando = "npm run dev"
    endereco = "http://localhost:5173/"

class Dependencias:
    react_router_DOM = "npm install react-router-dom"
    axios = "npm install axios"

class Esqueleto:
    def src(): return [
        "components",  # pasta
        "pages",       # pasta
        "context",     # pasta
        "services",    # pasta
        "styles",      # pasta (arquivos estáticos)
        "App.jsx"      # arquivo
    ]

class CssModules:
    nomenclatura_mandatoria_pro_arquivo = "nome do arquivo.module.css"
    local_criacao = "junto ao arquivo .jsx que ele irá servir"
    nome_obs = "na sintaxe de importação, o que vem após o [import] pode ter qualquer nome"
    forma_de_importar = 'import nomeCustomizado from "./nomeComponente.module.css"'  # mesmo nível, por isso ./
    obs = "as classes do css usadas, devem seguir a sintaxe de [camelCase] p/ evitar erros na chamada"

    # As chamadas acontecem dentro de {} usando notação ponto com o nome dado pra importação
    # O nome da importação dado aqui foi 'petOwner', então se chama: petOwner.nomeDaClasse
    exemplo_chamada = """
    .petOwnerFormArea:hover {
        box-shadow: 0 0 1.5rem #006363;
    }

    import petOwner from "./PetOwnerForm.module.css"

    function PetOwnerForm() {
        return (
            <>
            <div className={petOwner.petOwnerFormArea}>
            </div>
            </>
        )
    }
    """
    
    # P/ sintaxes múltiplas, se faz o mesmo, mas dentro de uma chave {`${petOwner.nomeClasseA} ${petOwner.nomeClasseB}`}
    # No exemplo dado, temos outro css usado, o 'resp', portanto é possível usar vários css externos juntos
    exemplo_chamada_multiplas_classes = """
    .petOwnerFormArea:hover {
        box-shadow: 0 0 1.5rem #006363;
    }

    import petOwner from "./PetOwnerForm.module.css"

    function PetOwnerForm() {
        return (
            <>
            <div className={`${resp.flex} ${resp.column} ${resp.goingCenter} ${resp.gapLG} ${petOwner.petOwnerFormArea}`}>
            </div>
            </>
        )
    }
    """

class ReactRouter:
    comando_instalacao = "npm install react-router-dom"
    arquivo_de_uso = "main.jsx"
    importacao = "import { createBrowserRouter, RouterProvider } from 'react-router-dom';"