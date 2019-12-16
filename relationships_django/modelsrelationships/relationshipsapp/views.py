from django.shortcuts import render
from . models import parents, childrens, game_playing 
# Create your views here.
def models_relationship(request):

# Let us understand these three lists. list_first contains father and it has three childrens and hence it would be many to many relationship. Coming to list_2 and list_3, each child has one game which he or she likes 
#     and hence it would come under foreign key concept

    list_first = ['father']
    list_second = ['son1', 'son2', 'daughter1']
    list_third = ['football', 'cricket', 'badminton']

    for parent in list_first:
        # saving the parent in the database
        p = parents()
        p.parent = parent
        p.save()
        
        for childs, games in zip(list_second, list_third):
            # saving the childrens belonging to parent in database
            child = childrens()
            child.children = childs
            child.save()
            # saving the game played by each children in the database
            game = game_playing()
            game.game_play = games
            game.game_child = child
            game.save()
            # saving the children association with parent
            p.childs.add(child)
            p.save()

