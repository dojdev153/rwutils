def format_phone(phone):
    phone = phone.strip()

    if phone.startswith("0"):
        phone = "+250" + phone[1:]

    if phone.startswith("+250"):
        number = phone[4:]

        if len(number) == 9 and number.isdigit():
            return f"+250 {number[:3]} {number[3:6]} {number[6:]}"

    raise ValueError("Invalid phone number format")