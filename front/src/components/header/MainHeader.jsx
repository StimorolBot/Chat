import "./style/main_header.sass"


export function MainHeader({ userName }) {

    return(
        <header className="header">
            <h3 className="header__user">
                { userName }
            </h3>
        </header>
    )
}