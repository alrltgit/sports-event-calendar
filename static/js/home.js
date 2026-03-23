async function loadHomeEvents() {
    const res = await fetch('/api/events');
    const events = await res.json()

    const current_dat = new Date();
    const liveContainer = document.getElementById('live-events');
    const upcomingContainer = document.getElementById('upcoming-events');

    liveContainer.innerHTML = '';
    upcomingContainer.innerHTML = '';

    events.sort((a, b) => new Date(a.date) - new Date(b.date));

    events.forEach(event => {
        const date = new Date(event.date)
        const formattedDate = date.toLocaleString(undefined, {
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit'
        });

        const div = document.createElement('div');
        div.className = 'event-card';

        div.innerHTML = `
            <div class="event-header">${event.competition}</div>
            <div class="event-participants">${event.participants || event.team}</div>
            <div class="event-meta">${formattedDate}</div>
        `;

        if (event.status === 'live') {
            liveContainer.appendChild(div)
        }

        if (event.status === 'scheduled' && upcomingContainer.children.length < 5) {
            upcomingContainer.appendChild(div.cloneNode(true));
        }
    })
}

loadHomeEvents();

document.addEventListener('DOMContentLoaded', () => {
    const newEvent = document.getElementById('add-event');
    const openBtn = document.querySelector('.add-event-btn');
    const closeBtn = document.querySelector('.close');
    const eventForm = document.getElementById('eventForm');

    openBtn.addEventListener('click', () => {
        newEvent.style.display = 'block';
    });

    closeBtn.addEventListener('click', () => {
        newEvent.style.display = 'none';
    });

    eventForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        let dateInput = document.getElementById('date').value;

        let dateObj = new Date(dateInput);

        let formattedDate = dateObj.getFullYear() + '-' +
            String(dateObj.getMonth() + 1).padStart(2, '0') + '-' +
            String(dateObj.getDate()).padStart(2, '0') + ' ' +
            String(dateObj.getHours()).padStart(2, '0') + ':' +
            String(dateObj.getMinutes()).padStart(2, '0') + ':' +
            String(dateObj.getSeconds()).padStart(2, '0');

        const eventData = {
            date: formattedDate,
            sport: document.getElementById('sport').value,
            competition: document.getElementById('competition').value,
            venue: document.getElementById('venue').value,
            location: document.getElementById('location').value,
            participants: document.getElementById('participants').value,
            status: 'scheduled'
        };

        console.log(eventData);

        try {
            const res = await fetch('/api/post_events', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(eventData)
            });

            const result = await res.json()

            newEvent.style.display = 'none';
            eventForm.reset();
            loadHomeEvents();
        } catch (err) {
            console.log('Error adding event:', err);
        }
    });
});
