import "./style/message.sass"

import cookies from "../../../config/cookies"


export function Message({ msg }){
    const cookieUuid = cookies.get("user_cookie")

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
                            <li className={ cookieUuid == m["user_id"]
                                ? "msg__item"
                                : "msg__item_other"} key={ i }>
                                { m["msg"] }
                            </li>)        
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
