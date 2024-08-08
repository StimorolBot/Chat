import "./style/main-btn.sass"


export function MainBtn({ children, ...props }) {
    return(
        <button className="main-btn" {...props}>
            { children }
        </button> 
    )
}