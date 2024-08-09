import "./style/message.sass"


export function Message({ msg }){
    
    return(
        <section className="section-message">
            <h2 className="hidden__title">
                Чат
            </h2>
            <div className="wrapper wrapper-msg">
                <ul id="msg__container">
                { msg !== undefined ?
                    msg.map((m, i) => {
                        return(
                        <li className="msg__item" key={ i }>{                   
                            m["msg"]
                        }</li>)        
                    })
                : <h3 className="msg__none">
                    Сообщений нет
                </h3>
                }
                </ul>
            </div>
        </section>
    )
}
