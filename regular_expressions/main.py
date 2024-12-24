import re
import csv
from pprint import pprint


def normalize_contacts(contacts):
    # Приведение ФИО к единому формату
    for contact in contacts[1:]:
        fio = " ".join(contact[:3]).split()
        contact[:3] = fio + [name for name in range(3 - len(fio))]

    # Приведение телефонов к формату +7(999)999-99-99 доб.9999
    phone_pattern = re.compile(r"""
    (\+?7|8)?
    \D*
    (\d{3})
    \D*
    (\d{3})
    \D*
    (\d{2})
    \D*
    (\d{2})
    (?:\D*доб\D*(\d+))?
  """, re.VERBOSE)
    for contact in contacts[1:]:
        phone = contact[-2]
        match = phone_pattern.search(phone)
        if match:
            formatted_phone = f"+7({match[2]}){match[3]}-{match[4]}-{match[5]}"
            if match[6]:  # Если найден дополнительный номер
                formatted_phone += f" доб.{match[6]}"
            contact[5] = formatted_phone

    # Объединение дублирующихся записей
    merged_contacts = {}
    for contact in contacts[1:]:
        key = f"{contact[0]} {contact[1]}"
        if key not in merged_contacts:
            merged_contacts[key] = contact
        else:
            for i in range(len(contact)):
                if not merged_contacts[key][i] and contact[i]:
                    merged_contacts[key][i] = contact[i]

    return [contacts[0]] + list(merged_contacts.values())

if __name__ == "__main__":
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    phone_book = normalize_contacts(contacts_list)

    # Сохранение данных в новый файл
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=",")
        datawriter.writerows(phone_book)