import "./style/main_aside.sass"

import { About } from "../section/About"
import { SearchUser } from "../section/SearchUser"
import { ChatRoom } from "../section/ChatRoom"


export function MainAside() {
    return(
        <aside className="aside">
            <div className="wrapper">
                <About/>
                <SearchUser/>    
                <ChatRoom/>
            </div>
        </aside>
    )
}