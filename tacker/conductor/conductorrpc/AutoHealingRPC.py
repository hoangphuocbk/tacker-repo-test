# Copyright 2017 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import oslo_messaging

from tacker.common import topics


class AutoHealingRPC(object):

    target = oslo_messaging.Target(
        exchange='tacker',
        topic=topics.TOPIC_CONDUCTOR,
        fanout=False,
        version='1.0')

    def vnf_respawning_event(self, context, **kwargs):
        pass
