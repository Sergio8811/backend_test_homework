class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(
            self,
            training_type: str,                 
            duration: float,
            distance: float,
            speed: float,
            calories: float
    ) -> None:
        self.training_type = training_type        
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (
            f'Тип тренировки: {self.training_type}; '
            f'Длительность: {self.duration:.3f} ч.; '
            f'Дистанция: {self.distance:.3f} км; '
            f'Ср. скорость: {self.speed:.3f} км/ч; '
            f'Потрачено ккал: {self.calories:.3f}.'
        )



class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    M_IN_HOUR = 60
    LEN_STEP = 0.65
    COEFF_CAL_RUN_ONE = 18
    COEFF_CAL_RUN_TWO = 20
    COEFF_CAL_WALK_ONE: float = 0.035
    COEFF_CAL_WALK_TWO: float = 0.029

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float
    ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        
    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        result = self.action * self.LEN_STEP / self.M_IN_KM
        return result

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = (
                (self.COEFF_CAL_RUN_ONE * self.get_mean_speed() - self.COEFF_CAL_RUN_TWO) * self.weight / self.M_IN_KM * self.duration * 60)
        return calories

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            type(self).__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories(),
        )


class Running(Training):
    """Тренировка: бег."""
    def get_spent_calories(self) -> float:
        return (self.COEFF_CAL_RUN_ONE * self.get_mean_speed() - self.COEFF_CAL_RUN_TWO) * self.weight / self.M_IN_KM * self.duration * self.M_IN_HOUR


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(
            self, action: int, duration: float, weight: float, height: float
    ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        return (self.COEFF_CAL_WALK_ONE * self.weight + (self.get_mean_speed() ** 2 // self.height) * self.COEFF_CAL_WALK_TWO * self.weight) * self.duration * Training.M_IN_HOUR


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38

    def __init__(
            self,
            action: int,
            duration: float,
            weight: float,
            length_pool: float,
            count_pool: float,
    ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration

    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + 1.1) * 2 * self.weight


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    exercise_type = {
        "SWM": Swimming,
        "RUN": Running,
        "WLK": SportsWalking,
    }
    kls = exercise_type.get(workout_type, None)
    return kls(*data) if kls else None


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    show_info = info.get_message()
    print(show_info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
