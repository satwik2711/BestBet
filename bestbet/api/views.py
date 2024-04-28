from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
import numpy as np

@api_view(['POST'])
def bestbet(request):

    try:
        data = request.data
        investment = float(data['investment'])
        t1_multiplier = float(data['t1_multiplier'])
        t2_multiplier = float(data['t2_multiplier'])
    except (KeyError, ValueError):
        return JsonResponse({'message': 'Invalid data format. Please provide investment, t1_multiplier, and t2_multiplier as floats.'}, status=status.HTTP_400_BAD_REQUEST)

    def find_optimal_split(investment, multiplier_A, multiplier_B):
        splits = np.linspace(0, 1, 101)  # Evaluate splits from 0% to 100% in 1% increments
        minimal_loss = float('inf')
        optimal_split = 0.5  # Default split

        for split in splits:
            bet_on_A = split * investment
            bet_on_B = (1 - split) * investment

            # Calculate potential losses
            loss_if_A_wins = investment - (bet_on_A * multiplier_A)
            loss_if_B_wins = investment - (bet_on_B * multiplier_B)

            # Determine the maximum loss in the worst case scenario
            worst_case_loss = max(loss_if_A_wins, loss_if_B_wins)

            # Update the optimal split if the current split has a lower worst case loss
            if worst_case_loss < minimal_loss:
                minimal_loss = worst_case_loss
                optimal_split = split

        return optimal_split, minimal_loss

    optimal_split, worst_case_loss = find_optimal_split(investment, t1_multiplier, t2_multiplier)
    bet_on_team_a = optimal_split * investment
    bet_on_team_b = investment - bet_on_team_a

    return JsonResponse({
        'optimal_split': optimal_split,
        'bet_on_team_a': bet_on_team_a,
        'bet_on_team_b': bet_on_team_b,
        'worst_case_loss': worst_case_loss,
        'message': 'Optimal split calculated to minimize the worst-case loss.'
    })
