import { createBrowserRouter } from "react-router-dom"

import { Chat } from "./page/Chat"
import { Register } from "./page/Register";


const router = createBrowserRouter([
    {
      path: "/",
      element: <Chat/>,
      children: [{
        path: ":id",
        element: <Chat/>,
      }]  
    },
    {
      path: "/register",
      element: <Register/>,
    },
    {
      path: "*",
      element: <h1>404</h1>,
    },
  ]);


export default router