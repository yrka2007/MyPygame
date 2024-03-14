from requests import delete
import datetime

print(delete('http://localhost:5000/api/jobs/3').json())