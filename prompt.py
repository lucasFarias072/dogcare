

class Problema:
    objetivo = "Eu quero conseguir acessar a rota de login, através do uso do React Router Dom"
    dificuldade = "Não sei usar o React Router Dom na versão 7"
    tipo_projeto = "React Router v7 com TypeScript"  # Dito por você em outros chats que não resolveram o problema
    objetivo_contextualizado = """
    * Eu estou conseguindo abrir a página que renderize os componentes: 
    * Eu presumo que isso esteja acontecendo pelo arquivo 'welcome.tsx' 
    * Eu abro a página índice com base nos dados da classe 'Organizacao'
      * Se você perceber, ele seguem um padrão de uso sequencial
      * Onde eu quero chegar é: eu quero clicar no botão de fazer login e DE FATO IR para a página de login
    """
    objetivo_posterior = "Criar as rotas de navegação seguintes, após desempacar do problema atual das rotas"

# Dados entre [] indicam arquivos nativos ou criados por mim
class Estrutura:
    raiz = [
        "app", "public [favicon.ico]", ".dockerignore", ".gitignore", "Dockerfile", "package-lock.json", "package.json", 
        "react-router.config.ts", "README.md", "tsconfig.json", "vite.config.ts", 
    ]

    app = [
        "routes [home.tsx, Index.tsx, Login.tsx, LoginBrick.tsx, PetOwnerForm.tsx]", 
        "welcome [welcome.tsx]",
        "root.tsx", "routes.ts"
    ]

class Organizacao:
    # Aqui, em específico, a importação não fui eu quem fiz, foi preenchida automaticamente pelo IDE
    welcome_tsx = """
    import { Index } from "~/pages/Index";

    export function Welcome() {
    return (
        <main>
        <div className="flex column going-center mh">
            <Index/>
        </div>
        </main>
    );
    }
    """

    index_tsx = """
    import '../assets/css/Adjusts.css'
    import '../assets/css/Flex.css'
    import '../assets/css/PetOwnerForm.css'
    import '../assets/css/Index.css'

    import { PetOwnerForm } from '../routes/PetOwnerForm'
    import { LoginBrick } from '../routes/LoginBrick'

    // import {Link} from "react-router"

    const Index = (): React.ReactElement => {
    return (
        <div id="container" className='flex column going-center gap-sm'>
        <h1 id="welcome-title">Bem-vindo ao DogCare</h1>
        <PetOwnerForm/>
        <LoginBrick/>
        </div>
    )
    }

    export {
        Index
    }
    """

    pet_owner_form_tsx = """
    import '../assets/css/Flex.css'
    import '../assets/css/General.css'
    import '../assets/css/PetOwnerForm.css'

    const PetOwnerForm = (): React.ReactElement => {
        return (
            <>
            <div id="pet-owner-form-area" className="flex column going-center gap-lg">
                <div>
                <h2 id="post-pet-owner-title">Cadastre-se como Tutor</h2>
                </div>

                <form action="#">
                <div className="flex column going-left gap-md">
                    <input className="ordinary-input" type="text" placeholder="Seu nome de tutor" required/>
                    <input className="ordinary-input" type="text" placeholder="Seu e-mail" required/>
                    <input className="ordinary-input" type="text" placeholder="Senha" required/>
                    <button id="post-new-pet-owner-btn">cadastrar</button>
                </div>
                </form>
                
            </div>
            </>
        )
    }

    export {
        PetOwnerForm
    }
    """
    
    login_brick_tsx = """
    import {Link} from 'react-router-dom'

    const LoginBrick = (): React.ReactElement => {
    return (
        <div className='flex row going-center gap-lg'>
            <h2 id="already-registered">Já possui sua conta?</h2>
            <p id="login-indicator">➜</p>
            <Link to="/login" id="post-login-btn">login</Link>
        </div>
    )
    }

    export {
        LoginBrick
    }
    """
