import "./style/main_header.sass"


export function MainHeader({ userName }) {

    return(
        <header className="header">
            <div className="wrapper">
                <h3 className="header__user">
                    { userName }
                </h3>
            </div>
        </header>
    )
}