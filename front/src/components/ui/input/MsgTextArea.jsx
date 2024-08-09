import "./style/msg_textarea.sass"

export function MsgTextArea({ innerRef }) {
    return(
        <textarea placeholder="Написать сообщение..." ref={ innerRef }
            className="msg-textarea" required spellCheck={true}>
        </textarea>
    )
}

