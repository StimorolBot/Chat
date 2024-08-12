import "./style/main_aside.sass"

import { About } from "../section/About"
import { SearchUser } from "../section/SearchUser"
import { ChatRoom } from "../section/ChatRoom"


export function MainAside({ userId, chatList, setChatList, setUserIdUrl, setMsg}) {
    
    return(
        <aside className="aside">
            <div className="wrapper wrapper-aside">
                <About userId={ userId } />
                <SearchUser chatList={ chatList } setChatList={ setChatList }/>    
                <ChatRoom chatList={ chatList } setUserIdUrl={ setUserIdUrl } setMsg={ setMsg }/>
            </div>
        </aside>
    )
}
