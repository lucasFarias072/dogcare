// import { type RouteConfig, index } from "@react-router/dev/routes";
import { type RouteConfig, route, index } from "@react-router/dev/routes";

export default [
    // index("routes/home.tsx")
    index("./routes/home.tsx"),
    route("login", "./routes/Login.tsx"),
    route("pet-owner-panel", "./routes/PetOwnerPanel.tsx")
] satisfies RouteConfig;
