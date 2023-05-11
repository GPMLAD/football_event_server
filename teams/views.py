from rest_framework.views import APIView, Response, Request, status
from .models import Team
from django.forms.models import model_to_dict
from teams.exceptions import (
    ImpossibleTitlesError,
    InvalidYearCupError,
    NegativeTitlesError,
)
from teams.utils import data_processing


# Create your views here.
class TeamView(APIView):
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()

        teams_list = [model_to_dict(team) for team in teams]

        return Response(teams_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        request_team = request.data

        try:
            data_processing(request_team)
        except NegativeTitlesError as error:
            return Response({"error": f"{error}"}, status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError as error:
            return Response({"error": f"{error}"}, status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError as error:
            return Response({"error": f"{error}"}, status.HTTP_400_BAD_REQUEST)

        team = Team.objects.create(**request_team)
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_201_CREATED)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
            team_dict = model_to_dict(team)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        return Response(team_dict, status.HTTP_200_OK)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()

        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
