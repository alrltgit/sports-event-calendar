let allEvents = [];

async function loadEvents() {
    const res = await fetch('/api/events');
    allEvents = await res.json();

    allEvents.sort((a, b) => new Date(a.date) - new Date(b.date));

    displayEvents(allEvents);
    fillFilterBySport();
}

function formatParticipants(event) {
    const participants = event.team.split(' vs ');

    if (participants.length > 2) {
        return `
            <div class="participants">
                <p>Participants:</p>
                <ul>
                    ${participants.map(p => `<li>${p}</li>`).join('')}
                </ul>
            </div>
        `;
    }

    return `
        <div class="participants">
            ${participants.join(' vs ')}
        </div>
    `;
}

function displayEvents(events) {
    const container = document.getElementById('events');
    container.innerHTML = '';

    events.forEach(event => {
        const date = new Date(event.date);
        const formattedDate = date.toLocaleString(undefined, {
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit'
        })

        const venueText =
            event.venue === '-' ? event.location :
            event.location === '-' ? event.venue :
            `${event.venue}, ${event.location}`

        const participantsHTML = formatParticipants(event);

        const div = document.createElement('div');
        div.className = 'event-card';

        div.innerHTML = `
            <div class="event-header">${participantsHTML}</div>
            <div class="event-meta">
                ${formattedDate}<br>
                Competition: ${event.competition}<br>
                Venue: ${venueText}
            </div>
            <div class="status ${event.status}">
                ${event.status.toUpperCase()}
            </div>
        `;
        container.appendChild(div);
    });
}

function filterEvents(status) {
    if (status === "all") {
        displayEvents(allEvents);
    } else {
        const filtered = allEvents.filter(e => e.status === status);
        displayEvents(filtered);
    }
}

function filterBySport(sport) {
    if (sport === "All") {
        displayEvents(allEvents);
    } else {
        const filtered = allEvents.filter(e => e.sports === sport);
        displayEvents(filtered);
    }
}

document.getElementById("filter").addEventListener("change", function () {
    const selectedSport = this.value;
    filterBySport(selectedSport);
});

loadEvents()
