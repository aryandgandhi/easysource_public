document.addEventListener('DOMContentLoaded', function() {
    const exploreBtn = document.getElementById('explore-btn');

    exploreBtn.addEventListener('click', function(event) {
        event.preventDefault();
        const target = document.getElementById('description');

        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
});