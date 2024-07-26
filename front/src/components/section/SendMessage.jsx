import "./style/send_message.sass"

import { SendMsgBtn } from "../ui/btn/SendMsgBtn"
import { MsgTextArea } from "../ui/input/MsgTextArea"


export function SendMessage() {
    const ws = new WebSocket(`http://localhost:8000/1cd57fe5-8878-436a-b85e-cc5ee2eed17f`)

    ws.onmessage = function(event) {
        let messages = document.getElementById('messages')
        let message = document.createElement('li')
        let content = document.createTextNode(event.data)
        message.appendChild(content)
        messages.appendChild(message)
    }

    const sendMsg = (event) => {
        event.preventDefault()
        let inputMsg = document.getElementById("text-msg")
        ws.send(JSON.stringify({"data": inputMsg.value, "chat_id":"1cd57fe5-8878-436a-b85e-cc5ee2eed17f"}))
        inputMsg.value = ""
    }

    return(
        <section className="section-send-message">
            <h2 className="hidden__title"> Отправка сообщений </h2>
            <form className="form-send-message" action="#" onSubmit={event => sendMsg(event)}>
                <MsgTextArea id="text-msg"/>
                <SendMsgBtn/>
            </form>
        </section>
    )
}

