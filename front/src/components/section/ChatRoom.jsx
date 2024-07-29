import "./style/chat_room.sass"


export function ChatRoom({ chatList }) {
    const createUrl = async (chatId, event) => {
        event.preventDefault()
        history.pushState("", "", chatId)   
    }

    return(
        <section className="chat-room">
            <h2 className="hidden__title">Чаты</h2>
            <div className="wrapper">
                <ul className="chat__container">
                    { chatList.length != 0 ?
                        chatList.map((chat, index) => {
                            return(
                                <li className="chat__item"
                                    key={ index } onClick={(event) => createUrl(chat, event)}>
                                    { chat }
                                </li>
                            )
                        })
                    : <h2>Список чатов пуст</h2>
                    }
                </ul>
            </div>
        </section>
    )
}
