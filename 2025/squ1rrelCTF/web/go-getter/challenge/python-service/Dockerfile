# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
FROM python:3.9-slim as chroot

RUN apt-get update && apt-get install -y socat

WORKDIR /usr/src/python-service

COPY . .
ENV FLAG=squ1rrel{fake_flag}

RUN pip install flask gunicorn

EXPOSE 8081

CMD ["python", "-m", "gunicorn", "--workers", "4", "-b", "0.0.0.0:8081", "app:app"]

