

# https://ccnlhopylxadrcbytaog.supabase.co
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNjbmxob3B5bHhhZHJjYnl0YW9nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQyODgzODQsImV4cCI6MjA3OTg2NDM4NH0.mOZmluy11bAQrxURmfchUW8lrYWEKOW_8C79V0GE3t4

class Contexto:
    objetivo = "Desejo incluir autenticação a este projeto"
    tipo_projeto = "React Router v7 com TypeScript"  # Dito por você em outros chats
    comportamento = """
    * Não esqueça de incluir todas as dependências necessárias para efetuar o procedimento
    * Por favor, tente não alucinar, eu lhe peço, por favor
    * Seja objetivo nas suas explicações
    """
    
# Dados entre [] indicam arquivos nativos ou criados por mim
class Estrutura:
    raiz = [
        "app", "public [favicon.ico]", ".dockerignore", ".gitignore", "Dockerfile", "package-lock.json", "package.json", 
        "react-router.config.ts", "README.md", "tsconfig.json", "vite.config.ts", 
    ]

    app = [
        "routes [home.tsx, Index.tsx, Login.tsx, LoginBrick.tsx, PetOwnerForm.tsx]", 
        "welcome [welcome.tsx]",
        "root.tsx", 
        "routes.ts"
    ]

class OrganizacaoRoutesPasta:
    # Aqui, em específico, a importação não fui eu quem fiz, foi preenchida automaticamente pelo IDE
    welcome_tsx = """
    import Index from "~/routes/Index";

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

    import  PetOwnerForm  from './PetOwnerForm'
    import  LoginBrick from './LoginBrick'

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

    export default Index
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
                    <input className="ordinary-input" type="email" placeholder="Seu e-mail" required/>
                    <input className="ordinary-input" type="text" placeholder="Senha" required/>
                    <button id="post-new-pet-owner-btn">cadastrar</button>
                </div>
                </form>
                
            </div>
            </>
        )
    }

    export default PetOwnerForm
    """
    
    login_brick_tsx = """
    import {Link} from 'react-router'

    const LoginBrick = (): React.ReactElement => {
    return (
        <div className='flex row going-center gap-lg'>
            <h2 id="already-registered">Já possui sua conta?</h2>
            <p id="login-indicator">➜</p>
            <Link to="/login" id="post-login-btn">login</Link>
        </div>
    )
    }

    export default LoginBrick
    """

    pet_owner_panel_tsx = """
    import '../assets/css/Adjusts.css'
    import '../assets/css/Flex.css'
    import '../assets/css/PetOwnerPanel.css'

    import PetPostForm from './PetPostForm';

    // import {Link} from 'react-router'
    import { useState } from 'react';

    const PetOwnerPanel = (): React.ReactElement => {
    const [mostrarForm, setMostrarForm] = useState(false);

    return (
        <div id="container" className='flex column going-center gap-sm mh'>
        <h1 id="user-area">Área do usuário</h1>
        <div id="labels-area" className="flex row going-center gap-lg">
            <p id="pet-logo">🐶</p>
            <h2>Seus pets</h2>
        </div>

        {/* Aqui, seria a div p/ inserir os dados dinâmicos */}
        <div id="pets-from-user-session" className='flex row going-left gap-sm'>
            <div className="pet-card flex column gap-sm">
                <p className="pet-name">Nome: Tonhão</p>
                <p className="pet-breed">Raça: Beagle</p>
                <p className="pet-register-date">Registro: 09/10/2025</p>
                <p className="pet-birth">Nascimento: 12/02/2021</p>
            </div>
            <div className="pet-card flex column gap-sm">
                <p className="pet-name">Nome: Roberto Carlos</p>
                <p className="pet-breed">Raça: Golden Retriever</p>
                <p className="pet-register-date">Registro: 17/10/2025</p>
                <p className="pet-birth">Nascimento: 26/08/2019</p>
            </div>
        </div>

        <button id="add-new-pet-form-btn" onClick={() => setMostrarForm(!mostrarForm)}>✚</button>

        {mostrarForm && (
            <PetPostForm/>
        )}

        </div>
    )
    }

    export default PetOwnerPanel
    """

    pet_post_form_tsx = """
    import '../assets/css/Flex.css'
    import '../assets/css/General.css'
    import '../assets/css/PetPostForm.css'

    const PetPostForm = (): React.ReactElement => {
        return (
            <>
                <form>
                    <div className='flex row going-center gap-sm'>
                        <button id="pet-post-btn" type="submit">incluir</button>
                        
                        <div className='flex column gap-sm'>
                            <input className="ordinary-input-c" type="text" placeholder="Nome do seu pet" />
                            <input className="ordinary-input-c" type="text" placeholder="Raça do seu pet" />
                            <input className="ordinary-input-c" type="text" placeholder="Quando nasceu (DD/MM/YY)" />
                        </div>
                        
                    </div>
                </form>
            </>
        )
    }

    export default PetPostForm
    """
    
    return_btn_tsx = """
    import '../assets/css/Flex.css'
    import '../assets/css/ReturnBtn.css'
    import {Link} from 'react-router'

    const ReturnBtn = (): React.ReactElement => {
    return (
        <div id='return-btn-container' className='flex row going-center'>
        <Link to='/' id='return-btn'>voltar</Link>
        </div>
    )
    }

    export default ReturnBtn
    """

class OrganizacaoROutesArquivo:
    """
    import { type RouteConfig, route, index } from "@react-router/dev/routes";

    export default [
        // index("routes/home.tsx")
        index("./routes/home.tsx"),
        route("login", "./routes/Login.tsx"),
        route("pet-owner-panel", "./routes/PetOwnerPanel.tsx")
    ] satisfies RouteConfig;
    """
