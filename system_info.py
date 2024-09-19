# Для получения данных о установленном дистрибутиве: cat /etc/*-release

import os
import shutil


def get_cpu_info() -> str:
    # Возвращает общую информацию о процессоре
    cpu_info = "--- Информация о процессоре ---\n"

    # Извлечение архитектуры
    uname_arch = os.uname().machine
    cpu_info += f"Архитектура: {uname_arch}\n"

    with open("/proc/cpuinfo", "r") as f:
        for line in f:
            if line == "processor\t: 1\n":
                break

            if "model name" in line:
                cpu_info += f"Модель: {line.split(":")[1].strip()}\n"
            elif "cpu cores" in line:
                cpu_info += f"Количество ядер: {line.split(":")[1].strip()}\n"
            elif "siblings" in line:
                cpu_info += f"Количество потоков: {line.split(":")[1].strip()}\n"
            elif "cache size" in line:
                cpu_info += f"L3 кэш: {line.split(":")[1].strip()}\n"

    return cpu_info


def get_disk_usage(path="/") -> str:
    # Возвращает информацию о дисковом пространстве
    total, used, free = shutil.disk_usage(path)

    return (
        f"--- Дисковое пространство ---\n"
        f"Всего места: {round(total / (2 ** 30), 2)} Гб\n"
        f"Использовано: {round(used / (2 ** 30), 2)} Гб\n"
        f"Свободно: {round(free / (2 ** 30), 2)} Гб\n"
    )

def get_memory_info():
    """Возвращает общее количество памяти, свободное, занятое и частоту памяти."""
    mem_info = "--- Информация о памяти ---\n"
    with open("/proc/meminfo", "r") as f:
        for line in f:
            if "MemTotal" in line:
                mem_info += f"Общая память: {int(line.split(":")[1].strip().split()[0]) // 1024} Мб\n"
            elif "MemFree" in line:
                mem_info += f"Свободная память: {int(line.split(":")[1].strip().split()[0]) // 1024} Мб\n"
            elif "MemAvailable" in line:
                mem_info += f"Доступная память: {int(line.split(":")[1].strip().split()[0]) // 1024} Мб\n"
            elif "Active:" in line:
                mem_info += f"Используемая память: {int(line.split(":")[1].strip().split()[0]) // 1024} Мб\n"

    # Частота памяти может не быть прямо доступной в meminfo, но можно попробовать извлечь из lshw
    try:
        from subprocess import check_output
        lshw_output = check_output(["lshw", "-C", "memory"]).decode("utf-8").splitlines()
        for line in lshw_output:
            if "size" in line and "clock" in line:
                mem_info += f"Частота памяти: {line.split()[3].strip()} МГц"
    except Exception:
        mem_info += "Частота памяти: Н/Д"

    return mem_info

