#
# SPDX-License-Identifier: Apache-2.0
#
# Copyright 2020 Andrey Pleshakov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from unittest.mock import NonCallableMock

from thespiae.conf.core import ConfigProcessor
from thespiae.conf.system import AppDataReader

app_data_reader = NonCallableMock(spec_set=AppDataReader)
config_processor = ConfigProcessor(app_data_reader)

real_app_data_reader = AppDataReader()
