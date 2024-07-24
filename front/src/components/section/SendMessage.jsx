import "./style/send_message.sass"

import { SendMsgBtn } from "../ui/btn/SendMsgBtn"
import { MsgTextArea } from "../ui/input/MsgTextArea"


export function SendMessage() {
    // забирать ид из рла
    const ws = new WebSocket(`http://localhost:8000/ee58e1ba-abf4-432a-a22b-f500235c18e4`)

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
        ws.send(JSON.stringify({"data": inputMsg.value, "id": userId}))
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

