import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Home from './pages/Home'
import Wormhole from './pages/Wormhole'
// import { BrowserRouter as Router, Route, Switch} from 'react-router-dom';

function App() {
    const [count, setCount] = useState(0)

    return (
        <div>
          {/* <Home /> */}
          <Wormhole />
        </div>
    )
}

export default App


// import React from 'react';
// import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
// import Wormhole from './pages/Wormhole'; // Import the Wormhole page
// import Home from './pages/Home'; // Your existing home page

// const App = () => {
//     return (
//         <Router>
//             <Switch>
//                 <Route path="/" exact component={Home} />
//                 <Route path="/wormhole" component={Wormhole} />
//                 {/* Add other routes as needed */}
//             </Switch>
//             <Link to="/wormhole">Travel to Wormhole</Link> {/* Link to navigate to the wormhole page */}
//         </Router>
//     );
// };

// export default App;