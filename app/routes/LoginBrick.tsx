

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
