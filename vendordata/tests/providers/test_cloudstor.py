# Copyright 2018 Australian Research Data Commons
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

import mock

from vendordata import test
from vendordata.tests import fakes

from vendordata.providers.cloudstor import CloudStorProvider


class TestCloudStorProvider(test.TestCase):

    def test_cloudstor_name(self):
        provider = CloudStorProvider(fakes.METADATA, mock.Mock())
        self.assertEqual(provider.name, 'cloudstor')

    def test_cloudstor_creds(self):
        provider = CloudStorProvider(fakes.METADATA, mock.Mock())
        with mock.patch.object(provider, 'keystone_client') as mock_kclient:
            cred = fakes.FakeCredential()
            mock_kclient.credentials.list.return_value = [cred]
            output = provider.run()
            expected = fakes.FAKE_CREDS
            self.assertEqual(expected, output)

    def test_cloudstor_creds_other_project(self):
        provider = CloudStorProvider(fakes.METADATA, mock.Mock())
        with mock.patch.object(provider, 'keystone_client') as mock_kclient:
            cred = fakes.FakeCredential(project_id='different_project')
            mock_kclient.credentials.list.return_value = [cred]
            output = provider.run()
            self.assertIsNone(output)
