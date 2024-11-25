import os
import unittest

from conans.client.rest.auth_manager import RemoteCreds

from conan.api.model import Remote
from conan.internal.api.remotes.localdb import LocalDB
from conan.test.utils.test_files import temp_folder


class AuthManagerUnitTest(unittest.TestCase):
    def setUp(self):
        tmp_dir = temp_folder()
        db_file = os.path.join(tmp_dir, "dbfile")
        self.localdb = LocalDB(db_file)

    def test_remotecreds_get_return_unset_if_auth_token_not_set(self):
        remote = Remote("foo", "foo.url")
        remote_creds = RemoteCreds(self.localdb).get(remote)
        self.assertEqual(remote_creds[1], "unset")
