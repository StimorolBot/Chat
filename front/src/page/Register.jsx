import "./style/register.sass"

import api from "../../config"
import cookies from "../../config"
import { useState } from "react"
import { MainInput } from "../components/ui/input/MainInput"
import { MainBtn } from "../components/ui/btn/MainBtn"


export function Register() {
    const [userData, setUserData] = useState([{
        "user_name": "","ttl": ""
    }])

    const sendData = async (event) => {
        event.preventDefault()
        await api.post("/register", userData).then((response) => {
            console.log(response)
            cookies.set(
                "userId", response.data["user_id"],
                { maxAge: response.data["ttl"] }
            )
        }).catch((error) => {
            console.log(error)
        })
    }


    return(
        <section className="register">
            <h2 className="register__title">
                Форма для регистрации
            </h2>
            <form className="register__form" action="" method="POST">
                <h2 className="register__form-title">Регистрация</h2>
                <div className="input-wrapper">
                    <MainInput id="username" type="text"
                        placeholder="Введите имя" required lblTitle={ "Имя" } 
                        onChange={(event) => setUserData({...userData, user_name: event.target.value})}
                    />
                </div>
                <div className="input-wrapper">
                    <MainInput id="password" type="text" lblTitle={"Время действия аккаунта"}
                        placeholder="Время действия аккаунта"
                        onChange={(event) => setUserData({...userData, ttl: event.target.value})}
                    />
                </div>
                <MainBtn onClick={(event) => sendData(event)}>
                    Зарегистрироваться
                </MainBtn>
            </form>
        </section>
    )
}
