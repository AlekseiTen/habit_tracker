from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit
from users.models import User


class HabitAPITests(APITestCase):
    def setUp(self):
        """Некая фикстура для тестов всех методов"""
        self.user = User.objects.create(email="admin@mail.ru", password="123")
        self.habit = Habit.objects.create(
            user=self.user,
            place="Спортзал",
            time="2024-12-11 17:27:00+03",
            duration=30,
            periodicity=1,
            action="Тренировки",
            pleasant_habit=True,
            reward=None,
            is_public=True,
        )
        self.create_url = "/habits/create/"
        # self.update_url = f"/{self.habit.id}/update/"
        # self.delete_url = f"/{self.habit.id}/delete/"
        # self.my_habits_url = "/my_habits/"
        # self.public_url = "/public/"
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        """Тест на создание привычки, и проверки кол-ва в базе"""
        data = {
            "time": "2024-12-11 17:27:00+03",
            "duration": 15,
            "periodicity": 3,
            "action": "кофе",
            "is_public": True,
            "place": "home sweet home",
            "reward": "Шоколадка",
            "user": self.user,
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)
