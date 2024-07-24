import "./style/message.sass"


export function Message() {
    return(
        <section className="section-message">
            <h2 className="hidden__title">
                Чат
            </h2>
            <ul id='messages'></ul>
        </section>
    )
}