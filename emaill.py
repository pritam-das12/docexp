from trycourier import Courier


def send_email(email, ans, auth):
    client = Courier(auth_token=auth)
    client.send_message(
        message={
            "to": {
                "email": f"{email}",
            },
            "content": {
                "title": f"Answer from Document-Explorer",
                "body": f"Hey ! \n Check out the answer to your question below. \nDo not reply back to this email. \n\n {ans}\nRegards\nResearch Buddy",
            },
            "data": {"note": f"\nDo not reply back to this email. \n\n {ans}\nRegards,\nDocument Explorer",
                     },
            "routing": {
                "method": "single",
                "channels": ["email"],
            },
        }
    )
    return True
