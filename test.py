import uuid, requests, json
requests.post(
    "https://api.todoist.com/rest/v1/tasks",
    data=json.dumps({
        "content": "Appointment with Maria",
        "due_string": "tomorrow at 12:00",
        "due_lang": "en",
        "priority": 4
    }),
    headers={
        "Content-Type": "application/json",
        "X-Request-Id": str(uuid.uuid4()),
        "Authorization": "Bearer d3d86f465e230a67f4328142a7783fb75d2d8d02"
    }).json()


{
    "comment_count": 0,
    "completed": false,
    "content": "Appointment with Maria",
    "due": {
        "date": "2016-09-01",
        "datetime": "2016-09-01T11:00:00Z",
        "string": "2017-07-01 12:00",
        "timezone": "Europe/Lisbon"
    },
    "id": 123,
    "order": 20,
    "priority": 4,
    "project_id": 234,
    "url": "https://todoist.com/showTask?id=123"
}
