function onProjectClick(projectId) {
    fetch(`/api/project/${projectId}/`)
    .then(response => response.json())
    .then(data => {
        let projectDiv = document.getElementById('project-details');
        projectDiv.style.display = 'block'; // Show the project details div
        projectDiv.innerHTML = `
            <h2>${data.name}</h2>
  
            <p>${data.description}</p>
            <h3>Summary</h3>
            <ul>${data.summary.split('\n').map(line => `<li>${line}</li>`).join('')}</ul>
            <h3>Issues</h3>
            ${data.issues.map(issue => `
                <div class="issue">
                    <h4>${issue.title}</h4>
                    <p>${issue.description}</p>
                    <h4>Summary</h4>
                    <ul class="bard-summary">${issue.bard_summary.split('.').map(line => `<li>${line}</li>`).join('')}</ul>
                </div>`
            ).join('')}
        `;
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
    let loading = document.getElementById('loading');
    if (loading) {
        loading.style.display = 'block';
    }

    fetch(`/api/projects/${projectDifficulty}/`) // Use the projectDifficulty variable in the fetch URL
    .then(response => response.json())
    .then(projects => {
        if (loading) {
            loading.style.display = 'none';
        }
        let div = document.getElementById('projects');
        div.innerHTML = '';

        projects.forEach(project => {
            let projectDiv = document.createElement('div');
            projectDiv.className = 'project';
            let starClass = project.starred ? 'starred' : 'not-starred';
            projectDiv.innerHTML = `
                <h2><a href="#" onclick="onProjectClick(${project.id}); return false;">${project.name}</a></h2>
                <button class="star-button ${starClass}" onclick="toggleStar(${project.id}, this);">Star</button>
                <ul>${project.summary.split('.').map(line => `<li>${line}</li>`).join('')}</ul>`;
            div.appendChild(projectDiv);
        });
        
        });
    });

function toggleStar(projectId, starButton) {
    fetch(`/toggle_star/${projectId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // you would need to define getCookie function to get csrftoken from cookies
        },
        body: JSON.stringify({
            'project_id': projectId
        })
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then((data) => {
        if (data.starred) {
            starButton.classList.remove('not-starred');
            starButton.classList.add('starred');
        } else {
            starButton.classList.remove('starred');
            starButton.classList.add('not-starred');
        }
    })
    .catch((error) => {
        console.error('There has been a problem with your fetch operation:', error);
    });
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
