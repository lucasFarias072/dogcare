

import '../assets/css/Adjusts.css'
import "../assets/css/Flex.css"
import '../assets/css/General.css'
import '../assets/css/LoginForm.css'

// Adicionado (p/ React)
import { useState } from 'react'
import { useAuth } from '../AuthContext'
// Adicionado: useNavigate
import {useNavigate, Link} from 'react-router'

import ReturnBtn from './ReturnBtn'

// Retirado
/*
<div className='flex row going-center'>
  <Link to="/pet-owner-panel" id="post-login-within-btn">entrar</Link>
  <ReturnBtn/>
</div>
*/

const Login = (): React.ReactElement => {
  // Adicionado
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!email || !password) {
      alert('Por favor, preencha todos os campos');
      return;
    }

    setIsSubmitting(true);

    const result = await login(email, password);
    
    setIsSubmitting(false);

    if (result) {
      navigate('/pet-owner-panel');
    } else {
      alert('Erro ao fazer login. Tente novamente.');
    }
  };
    
  return (
    <>
      <div id="login-form-area" className="flex column going-center mh">
        <div id="login-form-area-within">
            <h2 id="post-login-title">Login - DogCare</h2>

            <form onSubmit={handleSubmit}>
              <div className="flex column going-center gap-md">

                <input 
                  className="ordinary-input-b" type="email" placeholder="ex.: seu_email@gmail.com" required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  disabled={isSubmitting}
                />
                
                <input 
                  className="ordinary-input-b" type="password" placeholder="Senha" required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  disabled={isSubmitting}
                />

                {/* Substituído por isso */}
                <button id="post-new-pet-owner-btn" type="submit"
                  disabled={isSubmitting}
                  style={{ opacity: isSubmitting ? 0.6 : 1 }}
                > {isSubmitting ? 'entrando...' : 'entrar'}
                </button>
                
              </div>
            </form>
            
            {/* Novo */}
            <div className='flex row going-center gap-lg'>
              <p>Não tem conta?</p>
              <Link to="/" style={{ color: '#4a90e2', textDecoration: 'underline' }}>Cadastre-se</Link>
            </div>

        </div>
      </div>
    </>
  )
}

export default Login