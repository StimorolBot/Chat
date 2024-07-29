import "./style/main_aside.sass"

import api from "../../../config/api"
import { About } from "../section/About"
import { SearchUser } from "../section/SearchUser"
import { ChatRoom } from "../section/ChatRoom"

import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"


export function MainAside() {
    const [userInfo, setUserInfo] = useState({"userId": "", "chatList": []})
    const navigate = useNavigate()
    
    useEffect(() => {(
        async () => {
            await api.get("/").then((response) => {
                setUserInfo({
                    userId: response.data.data["user_id"],
                    chatList: response.data.data["chat"]
                })
            }).catch((error) =>{
                navigate("/register")
            })
        })()
    }, [])

    return(
        <aside className="aside">
            <div className="wrapper wrapper-aside">
                <About userId={ userInfo["userId"] } />
                <SearchUser userInfo={ userInfo } setUserInfo={ setUserInfo }/>    
                <ChatRoom chatList={ userInfo["chatList"] }/>
            </div>
        </aside>
    )
}
