import "./style/about.sass"


export function About({userId}) {
    
    return(
        <section className="about">
            <h2 className="hidden__title">Об аккаунте</h2>
            <div className="wrapper">
                <h3>#{userId}</h3>
            </div>
        </section>
    )
}
