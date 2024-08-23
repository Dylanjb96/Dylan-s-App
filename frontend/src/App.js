import React from 'react'

import { Route, BrowserRouter as Router, Switch } from "react-router-dom"
import { AuthProvider } from './context/AuthContext'

import Homepage from './views/Homepage'
import Loginpage from './views/Loginpage'
import Message from './views/Message'
import MessageDetail from './views/MessageDetail'
import Navbar from './views/Navbar'
import Registerpage from './views/Registerpage'
import SearchUsers from './views/SearchUsers'
import Todo from './views/Todo'



function App() {
  return (
    <Router>
      <AuthProvider>
        < Navbar/>
        <Switch>
          <Route component={Loginpage} path="/login" />
          <Route component={Registerpage} path="/register" exact />
          <Route component={Homepage} path="/" exact />
          <Route component={Todo} path="/todo" exact />
          <Route component={Message} path="/inbox" exact />
          <Route component={MessageDetail} path="/inbox/:id" exact />
          <Route component={SearchUsers} path="/search/:username" exact />
        </Switch>
      </AuthProvider>
    </Router>
  )
}

export default App