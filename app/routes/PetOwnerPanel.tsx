

import '../assets/css/Adjusts.css'
import '../assets/css/Flex.css'
import '../assets/css/PetOwnerPanel.css'

// Adicionado
import { useAuth } from '../AuthContext'
import { ProtectedRoute } from '../ProtectedRoute'
import { supabase } from '../supabaseClient'
import type { Pet, Profile } from '../supabaseClient'

import PetPostForm from './PetPostForm';

// Adicionado: useEffect
import { useState, useEffect } from 'react';

// Retirado
/* 
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
*/

const PetOwnerPanel = (): React.ReactElement => {
  const [pets, setPets] = useState<Pet[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  
  // Estados do formulário
  const [petName, setPetName] = useState('');
  const [petBreed, setPetBreed] = useState('');
  const [petBirthDate, setPetBirthDate] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const { user, logout } = useAuth();
  const [mostrarForm, setMostrarForm] = useState(false);

  // Buscar pets do usuário
  const fetchPets = async () => {
    if (!user) return;

    try {
      setIsLoading(true);
      const { data, error } = await supabase
      .from('pets').select('*').eq('owner_id', user.id).order('created_at', { ascending: false });

      if (error) throw error;
      setPets(data || []);
    } catch (error) {
      console.error('Erro ao buscar pets:', error);
      alert('Erro ao carregar seus pets');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchPets();
  }, [user]);

  // Adicionar novo pet
  const handleAddPet = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!petName || !petBreed || !petBirthDate) {
      alert('Preencha todos os campos');
      return;
    }

    if (!user) return;

    console.log('User ID:', user.id);
    console.log('User ID tipo:', typeof user.id);

    setIsSubmitting(true);

    try {
      const petData = {
        owner_id: user.id,
        name: petName,
        breed: petBreed,
        birth_date: petBirthDate,
      };

      // DEBUG: Ver o que está sendo enviado
      console.log('Dados do pet:', petData);

      const { data, error } = await supabase
        .from('pets').insert(
          [{
            owner_id: user.id,
            name: petName,
            breed: petBreed,
            birth_date: petBirthDate,
          }]).select().single();

      if (error) throw error;

      // Adiciona o novo pet à lista
      setPets([data, ...pets]);
      
      // Limpa o formulário
      setPetName('');
      setPetBreed('');
      setPetBirthDate('');
      setMostrarForm(false);
      
      alert('Pet cadastrado com sucesso!');
    } catch (error: any) {
      
      console.error('Erro ao adicionar pet:', error);
      alert('Erro ao cadastrar pet: ' + error.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  // Deletar pet
  const handleDeletePet = async (petId: string) => {
    if (!confirm('Tem certeza que deseja remover este pet?')) return;

    try {
      const { error } = await supabase.from('pets').delete().eq('id', petId);

      if (error) throw error;

      setPets(pets.filter(pet => pet.id !== petId));
      alert('Pet removido com sucesso');
    } catch (error: any) {
      console.error('Erro ao deletar pet:', error);
      alert('Erro ao remover pet: ' + error.message);
    }
  };

  // Formatar data para exibição
  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('pt-BR');
  };

  const userSessioButton = (user: string | undefined) => {
    return (
      <div id="user-session" className='flex column going-left gap-sm'>
          <p id="user-info" style={{ fontSize: '0.9rem' }}>Logado como {user}!</p>
          <button onClick={logout}
            style={{
              padding: '0 1rem', background: 'crimson', color: 'white', border: 'none', borderRadius: '.5rem',
              cursor: 'pointer', letterSpacing: '2px'
            }}
          >
            sair
          </button>
        </div>
    )
  }

  return (
    <div id="container" className='flex column going-center gap-sm mh'>

      {/* Adicionado */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%', maxWidth: '800px' }}>
        {userSessioButton(user?.email)}
      </div>

      <h1 id="user-area">Área do usuário</h1>
      <div id="labels-area" className="flex row going-center gap-lg">
        <p id="pet-logo">🐶</p>
        <h2>Seus pets</h2>
      </div>

      {/* Dados retirados */}
      
      {isLoading ? (
        <p>Carregando seus pets...</p>
      ) : pets.length === 0 ? (
        <div className='flex column going-center gap-sm'>
          <p style={{ textShadow: '0 0 .5rem #a15245' , color: '#a15245', fontSize: '1rem' }}>Você ainda não cadastrou nenhum pet.</p>
          <p style={{ textShadow: '0 0 .5rem #a15245' , color: '#a15245', fontSize: '1rem' }}>Clique no botão ✚ abaixo para adicionar!</p>
        </div>
      ) : (
        <div id="pets-from-user-session" className='flex row going-left gap-sm' style={{ flexWrap: 'wrap' }}>
          {/* Lista de pets */}
          {pets.map(pet => (
            <div key={pet.id} className="pet-card flex column gap-sm" style={{ position: 'relative' }}>
              
              <button
                onClick={() => handleDeletePet(pet.id)}
                style={
                  {
                    position: 'absolute', top: '.6rem', right: '.3rem', fontSize: '1.4rem',
                    textShadow: '0 0 1rem black', cursor: 'pointer',  
                  }
                }
                title="remova esse pet"
              > ❌ </button>

              <p className="pet-name">Nome: {pet.name}</p>
              <p className="pet-breed">Raça: {pet.breed}</p>
              <p className="pet-birth">Nascimento: {formatDate(pet.birth_date)}</p>
              <p className="pet-register-date">Cadastrado em: {formatDate(pet.created_at)}</p>
            </div>
          ))}
        </div>
      )}

      <button id="add-new-pet-form-btn" onClick={() => setMostrarForm(!mostrarForm)}>{mostrarForm ? '✖' : '✚'}</button>

      {/* Removido: <PetPostForm/> */}
      {mostrarForm && (
        <form onSubmit={handleAddPet}>
          <div className='flex row going-center gap-sm'>
            
            <button id="pet-post-btn" type="submit"
              disabled={isSubmitting}
              style={{ opacity: isSubmitting ? 0.6 : 1 }}
            > {isSubmitting ? '...' : 'incluir'}
            </button>
            
            <div className='flex column gap-sm'>
              <input className="ordinary-input-c" type="text" placeholder="Nome do seu pet" 
                value={petName}
                onChange={(e) => setPetName(e.target.value)}
                disabled={isSubmitting}
              />

              <input className="ordinary-input-c" type="text" placeholder="Raça do seu pet" 
                value={petBreed}
                onChange={(e) => setPetBreed(e.target.value)}
                disabled={isSubmitting}
              />
              
              <input className="ordinary-input-c" type="date" placeholder="Data de nascimento"
                value={petBirthDate}
                onChange={(e) => setPetBirthDate(e.target.value)}
                disabled={isSubmitting}
              />
            </div>
          </div>
        </form>

      )}

    </div>
  )
}

const PetOwnerPanelAuth = (): React.ReactElement => {
  return (
    <ProtectedRoute>
      <PetOwnerPanel />
    </ProtectedRoute>
  )
}

export default PetOwnerPanelAuth
