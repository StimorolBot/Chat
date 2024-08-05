import "./style/chat_room.sass"


export function ChatRoom({ chatList, setUserIdUrl }) {
    
    const createUrl = async (chatId) => {
        history.pushState("", "", chatId)
        setUserIdUrl(chatId)
    }

    return(
        <section className="chat-room">
            <h2 className="hidden__title">Чаты</h2>
            <div className="wrapper wrapper-chat-room">
                <ul className="chat__container chat__container_none">
                    { chatList.length != 0 ?
                        chatList.map((chat, index) => {
                            return(
                                <li className="chat__item"
                                    key={ index } onClick={(event) => createUrl(chat)}>
                                    { chat }
                                </li>
                            )
                        })
                    : <h2 className="chat__none">
                        Список чатов пуст
                    </h2>
                    }
                </ul>
            </div>
        </section>
    )
}
