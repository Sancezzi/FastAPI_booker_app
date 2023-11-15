import pytest

from app.hotels.dao import HotelDAO


@pytest.mark.parametrize("hotel_id,exist", [
    (1, True),
    (5, True),
    (7, False),
])
async def test_find_user_by_id(hotel_id, exist):
    hotel = await HotelDAO.find_one_or_none(id=hotel_id)

    if exist:
        assert hotel
        assert hotel["id"] == hotel_id
    else:
        assert not hotel
