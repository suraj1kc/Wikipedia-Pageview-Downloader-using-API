from django.shortcuts import render
from django.http import HttpResponse
import requests
import pandas as pd

def download_csv(request):
    if request.method == 'POST':
        url = request.POST.get('url')

        if url:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()["items"]
                df = pd.DataFrame(data, columns=["timestamp", "views"])
                df["timestamp"] = pd.to_datetime(df["timestamp"], format="%Y%m%d%H")
                df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%d")
                df.columns = ["Ds", "Y"]

                response = HttpResponse(content_type="text/csv")
                response["Content-Disposition"] = 'attachment; filename="pageviews.csv"'
                df.to_csv(response, index=False)

                return response

    return render(request, 'download.html')
