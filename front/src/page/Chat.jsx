import "./style/chat.sass"

import api from "../../config/api"
import { useNavigate } from "react-router-dom"
import { useEffect, useState } from "react"
import { MainAside } from "../components/aside/MainAside"
import { MainHeader } from "../components/header/MainHeader"
import { Message } from "../components/section/Message"
import { SendMessage } from "../components/section/SendMessage"


export function Chat() {

  const navigate = useNavigate()
  const [msgSend, setMsgSend] = useState(null)
  const [userIdUrl, setUserIdUrl] = useState("")

  const [userInfo, setUserInfo] = useState({
    "userId": "", "userName": "",
    "chatList": [], "msgList": []
  })

  useEffect(() => {(
    async () => {
        await api.get("/").then((response) => {
          setUserInfo({
            userId: response.data.data["user_id"],
            chatList: Object.values(response.data.data["chat_dict"]),
            msgList: response.data.data["msg_list"]?.["data"]["msg"]
          })
        }).catch((error) =>{
          if (error.response["status"] == 401){
            navigate("/register")
          } 
          else {
            console.log(error)
          }
        })
    })()
  }, [])
 
  return (  
    <div className="wrapper wrapper-body">
      <MainAside userId={ userInfo["userId"] }
        chatList={ userInfo["chatList"] }
        userInfo={ userInfo } 
        setUserInfo={ setUserInfo } 
        setUserIdUrl={ setUserIdUrl }
      />

      { userIdUrl.length != 0 ?
        <main className="main">
          <MainHeader userName={userInfo["userName"]}/>
          <Message msg={ msgSend }
            msgList={ userInfo["msgList"] }
          />
            
          <SendMessage msgSend={ msgSend }
            setMsgSend={ setMsgSend }
            userIdUrl={ userIdUrl }
          />
        </main>
      : <div className="empty-chat">
          Сообщений пока нет
        </div>
      }
    </div>
  )
}
