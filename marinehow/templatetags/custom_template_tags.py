from django import template
from marinehow.models import Usuario
register = template.Library()


@register.inclusion_tag('marinehow/vote_buttons.html')
def vote_buttons(votable, request):
    if request.user.is_authenticated():
        return {'votable_id': votable.id,
                "votable_type": votable.__class__.__name__,
                "voted_up": votable.voted_up_by(Usuario.objects.get(id=request.user.usuario.id)),
                "voted_down": votable.voted_down_by(Usuario.objects.get(id=request.user.usuario.id)),
                "score": votable.get_score(),
                "request": request,
                }
    else:
        return {"score":votable.get_score()}
