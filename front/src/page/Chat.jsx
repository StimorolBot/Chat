import "./style/chat.sass"

import { useState } from "react"
import { MainAside } from "../components/aside/MainAside"
import { MainHeader } from "../components/header/MainHeader"
import { Message } from "../components/section/Message"
import { SendMessage } from "../components/section/SendMessage"


export function Chat() {
  const [msg, setMsg] = useState([])

  return (  
      <div className="wrapper wrapper-body">
        <MainAside/>
        <main className="main">
          <MainHeader />
          <Message msgList={ msg } />
          <SendMessage msg={ msg } setMsg={ setMsg }/>
        </main>
      </div>
  )
}

