import React from 'react';
import { useParams } from 'react-router-dom';

function EventDetail() {
    const { id } = useParams();
    return (
        <div>
            <h1>Event Details</h1>
            <p>Details for event ID: {id}</p>
        </div>
    );
}
export default EventDetail;