import "./style/main_aside.sass"

import { About } from "../section/About"
import { SearchUser } from "../section/SearchUser"
import { ChatRoom } from "../section/ChatRoom"


export function MainAside({ userId, chatList, userInfo, setUserInfo, setUserIdUrl}) {
    
    return(
        <aside className="aside">
            <div className="wrapper wrapper-aside">
                <About userId={ userId } />
                <SearchUser userInfo={ userInfo } setUserInfo={ setUserInfo }/>    
                <ChatRoom chatList={ chatList } setUserIdUrl={ setUserIdUrl }/>
            </div>
        </aside>
    )
}
