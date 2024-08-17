import "./style/send_message.sass"

import { useRef} from "react"
import { SendMsgBtn } from "../ui/btn/SendMsgBtn"
import { MsgTextArea } from "../ui/input/MsgTextArea"
import { useNavigate } from "react-router-dom"


export function SendMessage({ userIdUrl }) {
    let msgRef = useRef("")
    const msgId = Date.now()
    const navigate = useNavigate()

    const showMsg = (msg) => {
        let messages = document.getElementById("msg__container")
        let message = document.createElement('li')
        let content = document.createTextNode(msg)
        message.className = "msg__item"
        message.appendChild(content)
        messages.appendChild(message)
    }

    const ws = new WebSocket(`http://localhost:8000${userIdUrl}`)
    
    ws.onopen = function(e) { console.log("соединение установлено") }
    ws.onmessage = function(event) { showMsg(event.data) }
    
    ws.onerror = function(error) {
        // Соединение закрыто или не может быть открыто
        if (error.target.readyState == 3){
            console.log(error)
            // navigate("/")
        }
    }

    ws.onclose = function(event) {
        if (event.wasClean) {
            console.log(`[close] Соединение закрыто чисто, код=${event.code} причина=${event.reason}`);
        } else {
          // например, сервер убил процесс или сеть недоступна
          // обычно в этом случае event.code 1006
          console.log('[close] Соединение прервано');
        }
    }

    const sendMsgServer = (event) => {
        event.preventDefault()
        ws.send(JSON.stringify({ "data": msgRef.current.value, "id": msgId }))
        showMsg(msgRef.current.value)
        msgRef.current.value = ""
    }

    return(
        <section className="section-send-message">
            <h2 className="hidden__title"> Отправка сообщений </h2>
            <form className="form-send-message" action="#" onSubmit={event => sendMsgServer(event)}>
                <MsgTextArea innerRef={ msgRef }/>
                <SendMsgBtn/>
            </form>
        </section>
    )
}
