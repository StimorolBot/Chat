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
  
  const [msg, setMsg] = useState([])
  const [userId, setUerId] = useState("")
  const [userIdUrl, setUserIdUrl] = useState("/")
  const [chatList, setChatList] = useState([])
  
  useEffect(() => {(
    async () => {
        await api.get("/").then((response) => {
          setUerId(response.data.data["user_id"])
          setChatList([...response.data.data["chat_list"]])
        }).catch((error) =>{
          if (error.response?.["status"] == 401){
            navigate("/register")
          } 
          else {
            console.log(error)
          }
        })
    })()
    
    if (window.location.pathname != "/"){
      setUserIdUrl(window.location.pathname)
    }         
  }, [])

  return (  
    <div className="wrapper wrapper-body">
      <MainAside userId={ userId }
        chatList={ chatList }
        setChatList = { setChatList } 
        setUserIdUrl={ setUserIdUrl }
        setMsg={ setMsg }
      />

      { userIdUrl.length != 1 &&
        <main className="main">
          <MainHeader userName={"sss"}/>
          <Message msg={ msg }/>
          <SendMessage userIdUrl={ userIdUrl }/>
        </main>
      }
    </div>
  )
}
