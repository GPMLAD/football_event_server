## Description

API using Django Rest FrameworkWork to organize a football championship, where each team will represent a selection.

## Endpoints

| HTTP Method | Description    | Endpoint                |
| ----------- | -------------- | ----------------------- |
| POST        | Create team    | `/api/teams/`           |
| GET         | List teams     | `/api/teams/`           |
| GET         | Fiter per team | `/api/teams/<team_id>/` |
| PATCH       | Update team    | `/api/teams/<team_id>/` |
| DELETE      | Delete team    | `/api/teams/<team_id>/` |
