def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('vadim', 'novikov',
                             city = 'moscow',
                             country = 'russia',
                             instituit = 'rtu mirea'
)
print(user_profile)