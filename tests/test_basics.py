import music_graph
import versioneer


def test_version():
    assert music_graph.__version__ == versioneer.get_version()
