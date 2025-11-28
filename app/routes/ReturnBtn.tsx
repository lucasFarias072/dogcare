

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

