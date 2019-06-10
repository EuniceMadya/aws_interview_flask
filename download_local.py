import paramiko
import os
from stat import S_ISDIR as isdir

remote_dir = '/Users/madya/Documents/GitHub/aws_interview_flask/flask_project/download_simulation/'
local_dir = '/Users/madya/Documents/GitHub/aws_interview_flask/flask_project/download_simulation/local/'

HOST_IP='52.65.192.180'
