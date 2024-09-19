import system_info


if __name__ == "__main__":
    info_methods = [
        system_info.get_dist_info(),
        system_info.get_cpu_info(),
        system_info.get_memory_info(),
        system_info.get_disk_usage()
    ]

    for method in info_methods:
        print(method)

    ''' Имеет ли смысл делать так, как это сделано выше? :DDD
    print(system_info.get_dist_info())
    print(system_info.get_cpu_info())
    print(system_info.get_memory_info())
    print(system_info.get_disk_usage())
    '''
