import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://obscure-broccoli-6r7xxgx56vh5w6g-8000.app.github.dev/api/teams/')
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div>
      <h1>Teams</h1>
      <ul>
        {teams.map(team => (
          <li key={team._id}>{team.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Teams;