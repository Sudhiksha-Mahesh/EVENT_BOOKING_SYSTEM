import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import EventDetail from './pages/EventDetail';
import BookingPage from './pages/BookingPage';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/event/:id" element={<EventDetail />} />
                <Route path="/booking" element={<BookingPage />} />
            </Routes>
        </Router>
    );
}
export default App;