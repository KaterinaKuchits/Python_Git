# (вместо 1) Найти IP адрес спамера и количество отправленных им запросов
# по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

with open('nginx_logs.txt', 'r', encoding="utf-8") as f:
    remote_addr_list = [line[:line.find(' ')] for line in f]

addr_max = max(set(remote_addr_list), key=remote_addr_list.count)
print(addr_max, remote_addr_list.count(addr_max))