import "./style/send_msg_btn.sass"


export function SendMsgBtn ({...props }){
    return(
        <button className="btn-send-msg" {...props}>
            <img className="img__btn-send" src="/public/icon/btn_send.svg" alt="Отпраить" />
        </button>
    )
}
