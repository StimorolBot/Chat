import { useState } from "react";
import "./style/main_input.sass"

export function MainInput({id, lblTitle, ...props}){
    const [isActive, setIsActive] = useState(false)
    
    return(
        <>
            <input className={isActive ? "main-input_active" : "main-input"}
                id={ id } { ...props }  
            />
            <label className={isActive ? "main-lbl_active" : "main-lbl"} htmlFor={ id }
                onClick={() => setIsActive(state => !state)}>
                { lblTitle }
            </label>
        </>
    )
}