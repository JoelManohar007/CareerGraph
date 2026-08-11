const userSelect = document.getElementById("userSelect");
const recommendButton = document.getElementById("recommendButton");
const recommendationsSection = document.getElementById("recommendationsSection");
const recommendationsContainer = document.getElementById("recommendations");
const recommendationCount = document.getElementById("recommendationCount");
const userStatus = document.getElementById("userStatus");

const detailsSection = document.getElementById("detailsSection");
const selectedJobTitle = document.getElementById("selectedJobTitle");
const missingSkillsContainer = document.getElementById("missingSkills");
const careerPathContainer = document.getElementById("careerPath");

const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");
const searchResults = document.getElementById("searchResults");


async function loadUsers() {
    try {
        const response = await fetch("/api/users");

        if (!response.ok) {
            throw new Error("Failed to load users.");
        }

        const users = await response.json();

        userSelect.innerHTML = '<option value="">Select a user</option>';

        users.forEach(user => {
            const option = document.createElement("option");

            option.value = user.id;
            option.textContent =
                `${user.name} · ${user.experience_level}`;

            userSelect.appendChild(option);
        });

        userStatus.textContent = `${users.length} candidates available`;

    } catch (error) {
        userStatus.textContent = "Unable to load candidates";
        userStatus.classList.add("error");
        console.error(error);
    }
}


async function loadRecommendations() {
    const userId = userSelect.value;

    if (!userId) {
        alert("Please select a candidate first.");
        return;
    }

    recommendButton.disabled = true;
    recommendButton.textContent = "Analyzing...";

    recommendationsContainer.innerHTML =
        '<div class="empty">Finding connected career paths...</div>';

    recommendationsSection.classList.remove("hidden");

    try {
        const response =
            await fetch(`/api/recommendations/${userId}`);

        if (!response.ok) {
            throw new Error("Failed to load recommendations.");
        }

        const recommendations = await response.json();

        recommendationCount.textContent =
            `${recommendations.length} roles`;

        if (recommendations.length === 0) {
            recommendationsContainer.innerHTML =
                '<div class="empty">No career paths found.</div>';

            return;
        }

        recommendationsContainer.innerHTML = "";

        recommendations.forEach(job => {

            const card = document.createElement("article");

            card.className = "career-card";

            card.innerHTML = `
                <h4>${escapeHtml(job.job_title)}</h4>

                <div class="match-row">
                    <span>Skill match</span>
                    <span class="match">
                        ${job.match_percentage}%
                    </span>
                </div>

                <div class="progress">
                    <div
                        class="progress-bar"
                        style="width: ${Math.min(job.match_percentage, 100)}%"
                    ></div>
                </div>

                <div class="skill-count">
                    ${job.matching_skills} of
                    ${job.total_required}
                    required skills
                </div>

                <button
                    class="view-button"
                    data-job-id="${job.job_id}"
                    data-job-title="${escapeAttribute(job.job_title)}"
                >
                    Explore Career
                </button>
            `;

            recommendationsContainer.appendChild(card);
        });

        document.querySelectorAll(".view-button").forEach(button => {
            button.addEventListener("click", () => {
                const jobId = button.dataset.jobId;
                const jobTitle = button.dataset.jobTitle;

                exploreCareer(jobId, jobTitle);
            });
        });

    } catch (error) {
        recommendationsContainer.innerHTML =
            `<div class="empty error">
                ${escapeHtml(error.message)}
            </div>`;

    } finally {
        recommendButton.disabled = false;
        recommendButton.innerHTML =
            'Find Career Paths <span>→</span>';
    }
}


async function exploreCareer(jobId, jobTitle) {

    const userId = userSelect.value;

    if (!userId) {
        return;
    }

    detailsSection.classList.remove("hidden");

    selectedJobTitle.textContent = jobTitle;

    missingSkillsContainer.innerHTML =
        '<div class="empty">Checking your skill gap...</div>';

    careerPathContainer.innerHTML =
        '<div class="empty">Exploring graph connections...</div>';

    detailsSection.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });

    try {

        const [missingResponse, pathResponse] =
            await Promise.all([
                fetch(`/api/missing-skills/${userId}/${jobId}`),
                fetch(`/api/career-path/${userId}`)
            ]);

        if (!missingResponse.ok || !pathResponse.ok) {
            throw new Error("Unable to load career analysis.");
        }

        const missingSkills =
            await missingResponse.json();

        const careerPaths =
            await pathResponse.json();


        // Missing skills
        if (missingSkills.length === 0) {

            missingSkillsContainer.innerHTML =
                '<div class="empty">You already have all required skills for this role. 🎉</div>';

        } else {

            const skillList = document.createElement("div");

            skillList.className = "skill-list";

            missingSkills.forEach(skill => {

                const tag = document.createElement("span");

                tag.className = "skill-tag";

                tag.textContent = skill.skill_name;

                skillList.appendChild(tag);
            });

            missingSkillsContainer.innerHTML = "";

            missingSkillsContainer.appendChild(skillList);
        }


        // Career paths
        if (careerPaths.length === 0) {

            careerPathContainer.innerHTML =
                '<div class="empty">No connected career paths found.</div>';

        } else {

            const pathList = document.createElement("div");

            pathList.className = "path-list";

            const uniquePaths = new Set();

            careerPaths.forEach(path => {

                const pathText =
                    `${path.skill} → ${path.job} → ${path.technology} → ${path.project}`;

                if (uniquePaths.has(pathText)) {
                    return;
                }

                uniquePaths.add(pathText);

                const item = document.createElement("div");

                item.className = "path-item";

                item.innerHTML = `
                    <span>${escapeHtml(path.skill)}</span>
                    →
                    ${escapeHtml(path.job)}
                    →
                    <span>${escapeHtml(path.technology)}</span>
                    →
                    ${escapeHtml(path.project)}
                `;

                pathList.appendChild(item);
            });

            careerPathContainer.innerHTML = "";

            careerPathContainer.appendChild(pathList);
        }

    } catch (error) {

        missingSkillsContainer.innerHTML =
            `<div class="empty error">
                ${escapeHtml(error.message)}
            </div>`;

        careerPathContainer.innerHTML =
            '<div class="empty error">Unable to load career paths.</div>';
    }
}


async function searchGraph() {

    const term = searchInput.value.trim();

    if (!term) {
        searchResults.innerHTML =
            '<div class="empty">Enter something to search.</div>';
        return;
    }

    searchResults.innerHTML =
        '<div class="empty">Searching the graph...</div>';

    try {

        const response =
            await fetch(`/api/search?q=${encodeURIComponent(term)}`);

        if (!response.ok) {
            throw new Error("Search failed.");
        }

        const results = await response.json();

        if (results.length === 0) {

            searchResults.innerHTML =
                `<div class="empty">
                    No results found for "${escapeHtml(term)}".
                </div>`;

            return;
        }

        searchResults.innerHTML = "";

        results.forEach(result => {

            const item = document.createElement("div");

            item.className = "search-result";

            item.innerHTML = `
                <div class="type">
                    ${escapeHtml(result.type)}
                </div>

                <div class="name">
                    ${escapeHtml(result.name)}
                </div>
            `;

            searchResults.appendChild(item);
        });

    } catch (error) {

        searchResults.innerHTML =
            `<div class="empty error">
                ${escapeHtml(error.message)}
            </div>`;
    }
}


function escapeHtml(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}


function escapeAttribute(value) {
    return escapeHtml(value);
}


recommendButton.addEventListener(
    "click",
    loadRecommendations
);

searchButton.addEventListener(
    "click",
    searchGraph
);

searchInput.addEventListener(
    "keydown",
    event => {
        if (event.key === "Enter") {
            searchGraph();
        }
    }
);


loadUsers();