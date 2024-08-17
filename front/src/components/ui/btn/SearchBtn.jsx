export function SearchBtn ({ search }) {
    return(
        <button className="search-btn" onClick={(event) => search(event)}>
            <img className="search-btn__img" src="/public/icon/search.svg" alt="Поиск" />
        </button>
    )
}