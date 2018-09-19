# coding: utf-8

import django_filters
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pick
from .serializer import PickSerializer

from django.shortcuts import render
import numpy as np

# Create your views here.

class PickViewSet(APIView):
    def get(self, request, pk):
      if pk >= 4:
        user_pick_matrix = np.zeros((pk,20))
      else:
        user_pick_matrix = np.zeros((4,20))
      for pick in Pick.objects.all():
        user_pick_matrix[pick.user_id-1][pick.pick_id-1] = 1

      similarities = []
      target = user_pick_matrix[pk-1]

      for i, other_user in enumerate(user_pick_matrix):
        if i == pk-1:
          continue

        similarity = np.corrcoef(target, other_user)[0,1]
        if np.isnan(similarity):
            continue
        similarities.append((i, similarity))
      target_user_index = 0
      similarities = sorted(similarities, key=lambda s: s[1], reverse=True)

      target = user_pick_matrix[target_user_index]
      avg_target = np.mean(target)

      numerator = 0.0
      denominator = 0.0
      rankings = []

      for i in range(20):
        for similarity in similarities:
          if target[i] == 1:
            continue
          user_pick_vector = user_pick_matrix[similarity[0]]
          denominator += similarity[1]
          numerator += similarity[1]*(user_pick_vector[i] - np.mean(user_pick_vector))
        predict = avg_target + (numerator / denominator) if denominator > 0 else -1
        rankings.append((i+1, predict))
      rankings = sorted(rankings, key=lambda r: r[1], reverse=True)
      return Response(rankings)

