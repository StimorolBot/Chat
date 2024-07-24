import Cookies from "universal-cookie"

let cookies = new Cookies()
cookies.partitioned = true
cookies.httpOnly = true
cookies.someSite="none"

export default cookies

