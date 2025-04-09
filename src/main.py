from constant import BASE_URL


class TestBookings:
    def test_create_booking(self, auth_session, booking_data):

        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data_response = get_booking.json()
        assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert booking_data_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

    def test_put_booking(self, auth_session, booking_data, booking_data_upd):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        print(create_booking.json())

        update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=booking_data_upd)
        assert update_booking.status_code == 200, "Ошибка при обновлении бронирования"

        upd_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert upd_booking.status_code == 200

        assert booking_data_upd['firstname'] != booking_data['firstname'], "Обонвление имени не произошло"
        assert booking_data_upd['lastname'] != booking_data['lastname'], "Обонвление фамилии не произошло"
        assert booking_data_upd['totalprice'] != booking_data['totalprice'], "Обонвление стоимости не произошло"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

    def test_put_invalid(self, auth_session, booking_data, booking_data_invalid):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        put_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=booking_data_invalid)
        assert put_booking.status_code == 200

        assert put_booking.json()['firstname'] is not '', "При отправке пустой строки, обновление не должно проходить"
        assert put_booking.json()['lastname'] is not '', "При отправке пустой строки, обновление не должно проходить"
        assert put_booking.json()['totalprice'] is not '', "При отправке пустой строки, обновление не должно проходить"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

    def test_get_all(self, auth_session):
        get_all_booking = auth_session.get(f"{BASE_URL}/booking/")
        assert get_all_booking.status_code == 200
        assert get_all_booking.json() is not None, "Получен пустой список. Броней нет"

    def test_get_bookings(self, auth_session, booking_data):
        all_booking = auth_session.get(f"{BASE_URL}/booking/")
        ids_booking = all_booking.json()
        assert ids_booking is not None, "Брони отсутствуют"

    def test_get_unique(self, auth_session, booking_data):

        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")

        all_booking = auth_session.get(f"{BASE_URL}/booking/")
        booking_list = all_booking.json()
        booking_ids = [booking.get("bookingid") for booking in booking_list if isinstance(booking, dict)]

        assert booking_id in booking_ids, "ID букинга не найден в ответе"


