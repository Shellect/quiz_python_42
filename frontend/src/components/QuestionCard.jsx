import { useState, useEffect } from 'react';
import preloader from '../assets/images/preloader.gif';

export default function(){
    const [card, setCard] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(async () => {
        try {
            const response = await fetch('http://localhost:8000/api/v1/question');
            const data = await response.json();
            setCard(data)
        } catch (error) {
            setError(error);
        } finally {
            setLoading(false);
        }
    }, []);

    let questionText = card?.question ?? 'Question 1';
    let questionOptions = card?.answers.map((answer, key) => <div key={key} className="mt-3 p-3 border rounded answer">{answer}</div>)

    if (loading) {
        return (<img src={preloader} alt="preloader" />)
    }

    return (
        <div className="card box-shadow mt-4">
            <div className="card-title text-center mt-3">
                <h3 className="question">{ questionText }</h3>
            </div>
            <div className="card-body">
                { questionOptions }
            </div>
        </div>
    );
}