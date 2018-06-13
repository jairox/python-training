from django.views.generic import ListView
import requests


# Create your views here.


class DataApiResource (ListView):
    template_name = "list_crypto.html"

    def get_queryset(self):
        url = 'https://api.coinmarketcap.com/v2/ticker/'
        response = requests.get(url)
        res = response.json()['data'].values()
        sort_list = sorted(res, key=lambda item: item["quotes"]["USD"]["percent_change_24h"], reverse=True)
        return sort_list[:10]
