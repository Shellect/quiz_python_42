import { Outlet } from 'react-router';
import Navbar from '../components/Navbar';

export default function () {
    return(
        <>
            <Navbar />
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-md-8">
                        <Outlet />
                    </div>
                </div>
            </div>
        </>
    );
}