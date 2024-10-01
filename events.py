import docker
import datetime
import requests

client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')
webhook_url = "https://discordapp.com/api/webhooks/1290737163205607515/EVWuE3pUpfdoXJJ1VDNyX9EoU6JhRfxd8T7-ltcsCerR63lrfHD4mpD6PfWeWLekapH1"

for event in client.events(decode=True, filters={'event': 'die'}):
    container_id = event["id"]
    container_name = event["Actor"]["Attributes"]["name"]
    epoch_time = event["time"]
    date_time = datetime.datetime.fromtimestamp(epoch_time)


    payload = {'content': f'The container {container_name} (ID: {container_id}) has died at {date_time}'}

    print(payload)

    requests.post(webhook_url, data=payload)
