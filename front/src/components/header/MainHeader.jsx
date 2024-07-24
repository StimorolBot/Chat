import "./style/main_header.sass"


export function MainHeader() {
    // document.querySelector("#ws-id").textContent = client_id;

    return(
        <header className="header">
             <h2>Your ID: <span id="ws-id"></span></h2>
        </header>
    )
}