from typing import Optional, List

from django.shortcuts import get_object_or_404
from ninja import Router, ModelSchema

from .models import Legislation, Category

router = Router(tags=["legislations"])

class LegislationIn(ModelSchema):
    category: Optional[str] = None

    class Meta:
        model = Legislation
        fields = ["title", "description", "time", "fine", "points", "type"]

class LegislationOut(ModelSchema):
    category: Optional[str] = None

    class Meta:
        model = Legislation
        fields = ["id", "title", "description", "time", "fine", "points", "type"]

    @staticmethod
    def resolve_category(obj):
        return obj.category.title if obj.category else None


@router.get("/legislation/", response=List[LegislationOut])
def list_legislation(request):
    legislation = Legislation.objects.all()
    return legislation

@router.post("/legislation/", response=LegislationOut)
def create_legislation(request, payload: LegislationIn):
    category = get_object_or_404(Category, title=payload.category)
    legislation = Legislation.objects.create(
        title=payload.title,
        description=payload.description,
        time=payload.time,
        fine=payload.fine,
        points=payload.points,
        type=payload.type,
        category=category
    )
    return legislation
