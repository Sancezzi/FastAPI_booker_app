import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("room_id,date_from,date_to,booked_rooms,status_code", [
    (4, "2030-10-01", "2030-10-15", 3, 200),
    (4, "2030-10-02", "2030-10-16", 4, 200),
    (4, "2030-10-03", "2030-10-17", 5, 200),
    (4, "2030-10-04", "2030-10-18", 6, 200),
    (4, "2030-10-05", "2030-10-19", 7, 200),
    (4, "2030-10-06", "2030-10-20", 8, 200),
    (4, "2030-10-07", "2030-10-21", 9, 200),
    (4, "2030-10-08", "2030-10-22", 10, 200),
    (4, "2030-10-09", "2030-10-23", 10, 409),
    (4, "2030-10-10", "2030-10-24", 10, 409),
])
async def test_add_and_get_booking(
    room_id,
    date_from,
    date_to,
    status_code,
    booked_rooms,
    authenticated_ac: AsyncClient,
):
    response = await authenticated_ac.post("/api/v1/bookings", params={
        "room_id": room_id,
        "date_from": date_from,
        "date_to": date_to,
    })

    assert response.status_code == status_code

    response = await authenticated_ac.get("/api/v1/bookings")
    assert len(response.json()) == booked_rooms


async def test_get_and_delete_booking(authenticated_ac: AsyncClient):
    response = await authenticated_ac.get("/api/v1/bookings")
    existing_bookings = [booking["id"] for booking in response.json()]
    for booking_id in existing_bookings:
        response = await authenticated_ac.delete(
            f"/api/v1/bookings/{booking_id}",
        )

    response = await authenticated_ac.get("/api/v1/bookings")
    assert len(response.json()) == 0
