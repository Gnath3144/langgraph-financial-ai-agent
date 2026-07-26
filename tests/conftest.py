import sys
import types
mock_uuid = types.ModuleType("uuid_utils")
mock_uuid.compat = types.ModuleType("uuid_utils.compat")
def mock_uuid7():
    import uuid
    return uuid.uuid4()
mock_uuid.compat.uuid7 = mock_uuid7
sys.modules["uuid_utils"] = mock_uuid
sys.modules["uuid_utils.compat"] = mock_uuid.compat
