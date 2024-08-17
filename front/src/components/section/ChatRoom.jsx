import "./style/chat_room.sass"

import api from "../../../config/api"
import { Link } from "react-router-dom"


export function ChatRoom({ chatList, setUserIdUrl, setMsg }) {
    
    const getMsg = async (event, chatId) => {
        event.preventDefault()
        await api.get(`/chat/${chatId}`).then((response) => {
            console.log(response.data["data"]["msg"])
            setMsg(response.data["data"]["msg"])
        }).catch((error) => {
            console.log(error)
        })
        setUserIdUrl(`/${chatId}`)
    }

    return(
        <section className="chat-room">
            <h2 className="hidden__title">Чаты</h2>
            { chatList["id"] !== "" ?
                <ul className="chat__container">
                    { chatList.map((chat, index) => {
                        return(
                            <li className="chat__item" key={ index }
                                onClick={(event) => getMsg(event, chat["chat_id"])}>
                                
                                <Link className="chat__item-link" to={`/${chat["chat_id"]}`}>
                                    { chat["chat_name"] }
                                </Link>
                            </li>
                        )
                    })}
                </ul>
                : <ul className="chat__container_none">
                    <h2 className="chat__none">
                        Список чатов пуст
                    </h2>
                </ul>
                }
        </section>
    )
}
