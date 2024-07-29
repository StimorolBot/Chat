import "./style/search_user.sass"

import { useRef } from "react"
import api from "../../../config/api"
import { SearchBtn } from "../ui/btn/SearchBtn"
import { SearchInput } from "../ui/input/SearchInput"


export function SearchUser({userInfo, setUserInfo }) {
    let searchRef = useRef("")

    const search = async (event) => {
        event.preventDefault()

        await api.post("/", {"user_id": searchRef.current.value}).
            then(( response )=>{
                setUserInfo({
                    ...userInfo,
                    chatList: [...userInfo["chatList"], response.data.data["chat_id"]]
                })
            }).
            catch((error) => {
                console.log(error)
            })
            searchRef.current.value = ""
        }

    return(
        <section className="search-user">
            <h2 className="hidden__title">Поиск пользователей</h2>
            <form className="search-user-form" action="/" method="POST">
                <SearchInput innerRef={ searchRef }/>
                <SearchBtn search={ search } />
            </form>
        </section>
    )
}
