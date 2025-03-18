import React, { useEffect, useState } from "react";
import { getEvents } from "../services/api";

const EventList = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      const response = await getEvents();
      setEvents(response.data);
    };
    fetchEvents();
  }, []);

  return (
    <div>
      <h2>Event List</h2>
      <ul>
        {events.map((event) => (
          <li key={event.id}>
            {event.name} - {event.available_seats}/{event.total_seats} seats available
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EventList;
