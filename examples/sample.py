# This file was generated by liblab | https://liblab.com/

from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(access_token="YOUR_ACCESS_TOKEN", base_url=Environment.DEFAULT.value)

result = sdk.achievements.achievements_get_all_achievements(offset=8, count=2)

print(result)
