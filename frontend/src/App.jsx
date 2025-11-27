import QuestionCard from './components/QuestionCard';
import Root from './pages/Root';
import Registration from './pages/Registration';
import ErrorPage from './pages/ErrorPage';
import { createBrowserRouter } from "react-router";
import { RouterProvider } from "react-router/dom";

const router = createBrowserRouter([
    {
        path: "/",
        element: <Root />,
        errorElement: <ErrorPage />,
        children: [
            {
                index: true,
                element: <QuestionCard />
            },
            {
                path: "/registration",
                element: <Registration />
            }
        ]
    }

]);

export default function () {
    return (
        <RouterProvider router={router} />
    );
}