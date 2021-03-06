# -*- coding: utf-8 -+-
import graphene

from django.contrib.auth.models import User

from .types import CategoryType, CompetitionType, DroneType, OwnerType, PilotType

from drones.models import Competition, Drone, DroneCategory, Pilot


class Query(object):

    all_categories = graphene.List(CategoryType)
    all_drones = graphene.List(DroneType)
    all_pilots = graphene.List(PilotType)
    all_competitions = graphene.List(CompetitionType)
    all_owners = graphene.List(OwnerType)

    category = graphene.Field(
        CategoryType, id=graphene.Int(), name=graphene.String()
    )

    drone = graphene.Field(
        DroneType, id=graphene.Int(), name=graphene.String()
    )

    pilot = graphene.Field(
        PilotType, id=graphene.Int(), name=graphene.String()
    )

    competition = graphene.Field(
        CompetitionType, id=graphene.Int()
    )

    owner = graphene.Field(
        OwnerType,
        id=graphene.Int(),
        first_name=graphene.String(),
        last_name=graphene.String()
    )

    def resolve_all_categories(self, info, **kwargs):
        return DroneCategory.objects.all()

    def resolve_all_drones(self, info, **kwargs):
        return Drone.objects.select_related('drone_category').all()

    def resolve_all_pilots(self, info, **kwargs):
        return Pilot.objects.all()

    def resolve_all_competitions(self, info, **kwargs):
        return Competition.objects.all()

    def resolve_all_owners(self, info, **kwargs):
        return User.objects.all()

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return DroneCategory.objects.get(pk=id)

        if name is not None:
            return DroneCategory.objects.get(name=name)

        return None

    def resolve_drone(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Drone.objects.get(pk=id)

        if name is not None:
            return Drone.objects.get(name=name)

        return None

    def resolve_pilot(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Pilot.objects.get(id=id)

        if name is not None:
            return Pilot.objects.get(name=name)

        return None

    def resolve_competition(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Competition.objects.get(pk=id)

        return None

    def resolve_owner(self, info, **kwargs):
        id = kwargs.get('id')
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')

        if id is not None:
            return User.objects.get(id=id)

        if first_name is not None:
            return User.objects.get(first_name=first_name)

        if last_name is not None:
            return User.objects.get(last_name=last_name)

        return None
