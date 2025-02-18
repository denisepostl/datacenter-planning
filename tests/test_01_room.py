"""Test the Room Module"""

from datacenter.model.room import Room
from utilities import create_test_session

try:
    import datacenter
except ImportError:
    pass


def test_00(capsys):
    """Test module import."""
    assert datacenter
    assert datacenter.model

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""


def test_01_room(capsys):
    """Test Room."""
    session = create_test_session()
    room = datacenter.model.Room()
    room.room_name = "Room"
    session.add(room)
    session.commit()

    assert repr(room) == "Room:Room"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
