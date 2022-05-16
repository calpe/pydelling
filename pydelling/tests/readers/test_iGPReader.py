import unittest
from pydelling.readers import iGPReader
from pydelling.config import config
from pydelling.utils import test_data_path


class iGPReaderCase(unittest.TestCase):
    """
    This class tests the iGPReader[pydelling.readers.iGPReader.io.iGPReader.iGPReader] class implementation
    """
    def setUp(self) -> None:
        self.igp_reader = iGPReader(test_data_path() / "test_implicit_to_explicit.gid",
                                            project_name="test-implicit_to_explicit"
                                            )

    def test_implicit_to_explicit(self):
        self.igp_reader.build_mesh_data()
        self.igp_reader.implicit_to_explicit()


if __name__ == '__main__':
    unittest.main()