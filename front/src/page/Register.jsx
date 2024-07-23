import "./style/register.sass"

import api from "../../config/api"
import cookies from "../../config/cookies"

import { useState } from "react"
import { MainInput } from "../components/ui/input/MainInput"
import { MainBtn } from "../components/ui/btn/MainBtn"
import { useNavigate } from "react-router-dom"


export function Register() {
    const navigate = useNavigate()
    const [userData, setUserData] = useState([{
        "user_name": "","ttl": ""
    }])

    const sendData = async (event) => {
        event.preventDefault()
        await api.post("/register", userData).then((response) => {
            cookies.set(
                "user_cookie", response.data.data["user_id"],
                {
                    maxAge: response.data.data["ttl"],
                    path: "/"
                 }
            )
            navigate("/")
        }).catch((error) => {
            console.log(error)
        })
    }
    return(
        <section className="register">
            <h2 className="hidden__title">
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
