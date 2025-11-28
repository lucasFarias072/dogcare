

import '../assets/css/Flex.css'
import '../assets/css/General.css'
import '../assets/css/PetOwnerForm.css'

// Adicionado (p/ React)
import { useState } from 'react'
import { useAuth } from '../AuthContext'
import { useNavigate } from 'react-router'

const PetOwnerForm = (): React.ReactElement => {
  // Adicionado 
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!name || !email || !password) {
      alert('Por favor, preencha todos os campos');
      return;
    }

    const success = await register(name, email, password);
    
    if (success) {
      alert('Cadastro realizado com sucesso!');
      navigate('/pet-owner-panel');
    }
  };
  
  return (
      <>
        <div id="pet-owner-form-area" className="flex column going-center gap-lg">
          <div>
            <h2 id="post-pet-owner-title">Cadastre-se como Tutor</h2>
          </div>
          
          {/* antes: action="#" */}
          <form onSubmit={handleSubmit}>
            <div className="flex column going-left gap-md">

              {/* p/ cada input: value, onChange */}
              <input 
                className="ordinary-input" type="text" placeholder="Seu nome de tutor" 
                value={name}
                onChange={(e) => setName(e.target.value)} required
              />

              <input 
                className="ordinary-input" type="email" placeholder="Seu e-mail" 
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />

              <input 
                className="ordinary-input" type="password" placeholder="Senha" 
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />

              <button id="post-new-pet-owner-btn">cadastrar</button>
            </div>
          </form>
          
        </div>
      </>
  )

}

export default PetOwnerForm
