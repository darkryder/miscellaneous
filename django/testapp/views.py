from django.contrib.auth.decorators import login_required
from splunkdj.decorators.render import render_to

@render_to('testapp:home.html')
@login_required
def home(request):
    return {
        "data_files_list": [
            {
                "name": "researchers.csv",
                "main_token": "ResearchersPerMillionPopulation"
            },
            {
                "name": "gdp.csv",
                "main_token": "AnnualGrowthRate"
            },
        ]
    }