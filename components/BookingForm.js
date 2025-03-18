import React, { useState } from "react";
import { bookSeat } from "../services/api";

const BookingForm = () => {
  const [eventId, setEventId] = useState("");

  const handleBooking = async (e) => {
    e.preventDefault();
    try {
      const response = await bookSeat(eventId);
      if (response.status === 200) {
        alert("Seat booked successfully!");
      }
    } catch (error) {
      alert("Failed to book seat: " + error.response.data.detail);
    }
  };

  return (
    <form onSubmit={handleBooking}>
      <h3>Book a Seat</h3>
      <label>Event ID:</label>
      <input value={eventId} onChange={(e) => setEventId(e.target.value)} />
      <button type="submit">Book Seat</button>
    </form>
  );
};

export default BookingForm;
