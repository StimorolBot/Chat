import "./style/chat.sass"

import { MainAside } from "../components/aside/MainAside"
import { MainHeader } from "../components/header/MainHeader"
import { Message } from "../components/section/Message"
import { SendMessage } from "../components/section/SendMessage"


export function Chat() {
  return (  
      <div className="wrapper wrapper-body">
        <MainAside/>
        <main className="main">
          <MainHeader />
          <Message />
          <SendMessage />
        </main>
      </div>
  )
}

