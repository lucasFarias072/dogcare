

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
