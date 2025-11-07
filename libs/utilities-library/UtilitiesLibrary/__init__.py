from .DictManagement import DictManagement
from .Utilities import Utilities
from .DtManagement import DtManagement
from .XmlManagement import XmlManagement
from .SocketManagement import SocketManagement
from .TagGenerator import TagGenerator
from .__version__ import VERSION

__version__ = VERSION


class UtilitiesLibrary(DictManagement, Utilities, DtManagement, XmlManagement, SocketManagement, TagGenerator):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = __version__
