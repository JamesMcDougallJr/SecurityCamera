# SecurityCamera
A raspberry pi security cam

I put this together during my Winter break, 2019. It involved working with my home router to enable port forwarding, and learning its public ip address.
I then use this public IP to make GET requests to my pi, which is running a Flask server. This Flask server serves up the video frames.
It's somewhat delayed, by anywhere from 10-20 seconds. This is likely because of the slowness of the Raspberry Pi, or possibly my Nginx configuration, which redirects all Pi traffic to Flask.
Obviously, viewing the video feed directly is somewhat instantaneous, so it is likely some non-Flask code causing the issue.
I also got some great experience working with docker-compose to orchestrate the conversation between the Nginx reverse proxy and the Flask server.
