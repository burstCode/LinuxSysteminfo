# Для получения данных о установленном дистрибутиве: cat /etc/*-release

import os

def get_cpu_info() -> str:
    data_from_command = os.popen('lscpu').read().split()

    cpu_info = (
        f"--- Данные о процессоре ---\n"
        f"Модель процессора: {data_from_command[29]} {data_from_command[30]} {data_from_command[31]}\n"
        f"Архитектура: {data_from_command[1]}\n"
        f"Количество ядер: {data_from_command[19]}\n"
        f"Количество потоков: {int(data_from_command[19]) * int(data_from_command[43])}\n"
        f"Тактовая частота: {data_from_command[34]}\n"
        f"Объем кэша L2: {data_from_command[168]} {data_from_command[169]}\n"
        f"Объем кэша L3: {data_from_command[174]} {data_from_command[175]}\n"
    )

    return cpu_info
