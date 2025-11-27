import { createRoot } from 'react-dom/client';
import './assets/main.scss';
import * as bootstrap from 'bootstrap';
import App from './App';

const root = createRoot(document.getElementById('root'));
root.render(<App />);