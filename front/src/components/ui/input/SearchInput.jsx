import "./style/search_input.sass"

export function SearchInput ({ innerRef }){
    return(
        <input className="search-input" type="text" required
            placeholder="Поиск чатов..."
            ref={ innerRef } 
        />
    )
}