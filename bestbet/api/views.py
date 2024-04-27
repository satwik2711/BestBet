from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

def betting_strategy(t1_multiplier, t2_multiplier, investment):
    p1 = 1 / t1_multiplier
    p2 = 1 / t2_multiplier
    b1 = t1_multiplier - 1
    b2 = t2_multiplier - 1
    f1 = (b1 * p1 - (1 - p1)) / b1 if b1 != 0 else 0
    f2 = (b2 * p2 - (1 - p2)) / b2 if b2 != 0 else 0

    f1 = max(f1, 0)
    f2 = max(f2, 0)
    
    total_f = f1 + f2
    if total_f > 1:
        f1 /= total_f
        f2 /= total_f

    bet1 = f1 * investment
    bet2 = f2 * investment

    return bet1, bet2

@api_view(['POST'])
def bestbet(request):
    # Extract data from the POST request
    data = request.data
    t1_multiplier = float(data['t1_multiplier'])
    t2_multiplier = float(data['t2_multiplier'])
    investment = float(data['investment'])

    # Calculate the optimal bet amounts
    bet1, bet2 = betting_strategy(t1_multiplier, t2_multiplier, investment)

    # Return the response
    return Response({
        'bet_on_team1': bet1,
        'bet_on_team2': bet2
    })
