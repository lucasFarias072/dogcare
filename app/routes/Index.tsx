

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
