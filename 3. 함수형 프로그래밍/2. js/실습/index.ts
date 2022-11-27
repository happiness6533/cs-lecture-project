import { initRouter, Route } from "./core/BrowserRouter"; // 또는 HashRouter
import Main from "./pages/Main";
import Component from "@/core/Component";
import "./scss/index.scss";
import Sub from "./pages/Sub";

const routes: Route[] = [
    { path: "/", page: Main as typeof Component },
    { path: "/sub", page: Sub as typeof Component },
];

const $app = document.querySelector("#app") as HTMLElement;

initRouter({ $app, routes });